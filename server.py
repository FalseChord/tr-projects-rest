from eve import Eve
from eve.auth import TokenAuth
from flask import redirect, request, Response
from settings import posts, ASSETS_URL, GCS_URL, ENV
from werkzeug.security import check_password_hash
import json
import random
import string
import sys, getopt

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
    # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        return accounts.find_one({'token': token})

def add_token(documents):
    for document in documents:
        document["token"] = (''.join(random.choice(string.ascii_uppercase)
                                    for x in range(10)))

def get_full_relateds(item, key):
    if key in item and item[key]:
        headers = dict(request.headers)
        tc = app.test_client()
        all_relateds =  ",".join(map(lambda x: '"' + str(x["_id"]) + '"' if type(x) is dict else '"' + str(x) + '"', item[key]))
        resp = tc.get('posts?where={"_id":{"$in":[' + all_relateds + ']}}', headers=headers)
        resp_data = json.loads(resp.data)
        result = []
        for i in item[key]: 
            for j in resp_data['_items']:
                if (type(i) is dict and str(j['_id']) == str(i['_id'])) or j['_id'] == str(i):
                    result.append(j)
                    continue
        item[key] = result
        # item[key] = resp_data['_items']
    return item

def replace_imageurl(obj):
    for key in [ 'brief', 'content' ]:
        if key in obj:
            obj_str = json.dumps(obj[key])
            obj_str = obj_str.replace(GCS_URL, ASSETS_URL)
            obj[key] = json.loads(obj_str)
    if 'heroImage' in obj and isinstance(obj['heroImage'], dict) and  'image' in obj['heroImage']:
        image_str = json.dumps(obj['heroImage']['image'])
        image_str = image_str.replace(GCS_URL, ASSETS_URL)
        obj['heroImage']['image'] = json.loads(image_str)
    if 'heroVideo' in obj and isinstance(obj['heroVideo'], dict) and  'video' in obj['heroVideo']:
        video_str = json.dumps(obj['heroVideo']['video'])
        video_str = video_str.replace(GCS_URL, ASSETS_URL)
        obj['heroVideo']['video'] = json.loads(video_str)
    return obj

def before_returning_posts(response):
    related = request.args.get('related')
    clean = request.args.get('clean')
    items = response['_items']
    for item in items:
        if clean == 'content':
            if 'brief' in item:
                del item['brief']['draft']
                del item['brief']['apiData']
            if 'content' in item:
                del item['content']['draft']
                del item['content']['apiData']
        if item["style"] == 'script':
            script_parsing = item['content']['html']
            scenes = script_parsing.split("<p><code>page</code></p>")
            page_div = "".join(map(lambda x: '<div class="page">' + x + '</div>', scenes))
            item['content']['html'] = page_div
        replace_imageurl(item)
        if related == 'full':
            item = get_full_relateds(item, 'relateds')
    return response

def before_returning_meta(response):
    related = request.args.get('related')
    replace = request.args.get('replace')
    items = response['_items']
    for item in items:
        if replace != 'false':
            if 'brief' in item:
                del item['brief']['draft']
                del item['brief']['apiData']
            replace_imageurl(item)
        if related == 'full':
            item = get_full_relateds(item, 'relateds')
        else:
            if related == 'false' and 'relateds' in item:
                del item['relateds']
    return response

def before_returning_listing(response):
    for item in response['_items']:
        if 'brief' in item:
            if 'apiData' in item['brief']:
                del item['brief']['apiData']
        if 'brief' in item:
            if 'draft' in item['brief']:
                del item['brief']['draft']
        if '_updated' in item:
            del item['_updated']
        if '_created' in item:
            del item['_created']
        if '_links' in item:
            del item['_links']
        if 'writers' in item:
            del item['writers']
        if 'sections' in item:
            if 'javascript' in item['sections']:
                del item['sections']['javascript']
            if 'css' in item['sections']:
                del item['sections']['css']
            if 'categories' in item['sections']:
                del item['sections']['categories']

    return response

def before_returning_choices(response):
    for item in response['_items']:
        item = get_full_relateds(item, 'choices')
        for i in item['choices']:
            if 'content' in i:
                del i['content']
            if 'relateds' in i:
                del i['relateds']
            if 'brief' in i:
                if 'apiData' in i['brief']:
                    del i['brief']['apiData']
            if 'brief' in i:
                if 'draft' in i['brief']:
                    del i['brief']['draft']
            if 'writers' in i:
                del i['writers']
            if 'photographers' in i:
                del i['photographers']
            if 'camera_man' in i:
                del i['camera_man']
            if 'categories' in i:
                del i['categories']
            if 'tags' in i:
                del i['tags']
    return response

def before_returning_sections(response):
    items = response['_items']
    sortedItems = sorted(items, key = lambda x: x["sortOrder"])
    response['_items'] = sortedItems
    return response

def remove_extra_fields(item):
  accepted_fields = schema.keys()
  for field in item.keys():
    if field not in accepted_fields and field != '_id':
      del item[field]

def pre_GET(resource, request, lookup):
    isCampaign = request.args.get('isCampaign')
    if resource == 'posts' or resource == 'meta':
        if isCampaign:
            if isCampaign == 'true':
                lookup.update({"isCampaign": True})
            elif isCampaign == 'false':
                lookup.update({"isCampaign": False})
        elif isCampaign is None:
            lookup.update({"isCampaign": False})

#app = Eve(auth=RolesAuth)

if ENV == 'prod':
    app = Eve(auth=TokenAuth)
else:
    app = Eve()
app.on_replace_article += lambda item, original: remove_extra_fields(item)
app.on_insert_article += lambda items: remove_extra_fields(items[0])
app.on_insert_accounts += add_token
app.on_fetched_resource_posts += before_returning_posts
app.on_fetched_resource_meta += before_returning_meta
app.on_fetched_resource_listing += before_returning_listing
app.on_fetched_resource_choices += before_returning_choices
app.on_fetched_resource_sections += before_returning_sections
app.on_pre_GET += pre_GET

@app.route("/sections-featured", methods=['GET', 'POST'])
def get_sections_latest():
    response = { "_items": {},
                 "_links": { 
                            "self": { "href":"sections-latest", "title": "sections latest"}, 
                            "parent":{ "parend": "/", "title": "Home" } } }
    headers = dict(request.headers)
    content = request.args.get('content') or 'posts'
    tc = app.test_client()
    resp = tc.get('/sections', headers=headers)
    resp_header = dict(resp.headers)
    del headers['Content-Length']
    resp_data = json.loads(str(resp.data))
    section_items = resp_data["_items"]
    section_items = sorted(section_items, key = lambda x: x["sortOrder"])
    if ("_error" not in resp_data and "_items" in resp_data):
        for item in section_items:
            if (content == 'meta'):
                endpoint = 'meta'
            else:
                endpoint = 'posts'
            sec_resp = tc.get('/' + endpoint + '?where={"sections":"' + item['_id'] + '","isFeatured":true}&max_results=5&sort=-publishedDate', headers=headers)
            sec_items = json.loads(sec_resp.data)
            if '_error' not in sec_items and "_items" in sec_items:
                #response[item['name']] = sec_items['_items']
                for sec_item in sec_items:
                    replace_imageurl(sec_item)
                response['_items'][item['name']] = sec_items['_items']
    return Response(json.dumps(response), headers=resp_header)        
        
@app.route("/combo", methods=['GET'])
def handle_combo():
    endpoints = {'posts': '/posts?sort=-publishedDate&clean=content', 'sectionfeatured': '/sections-featured?content=meta', 'choices': '/choices?max_results=1&sort=-pickDate',\
     'meta': '/meta?sort=-publishedDate&clean=content&related=full', 'sections': '/sections', 'topics':'/topics?sort=sortOrder', 'posts-vue': '/listing?sort=-publishedDate&clean=content&max_results=20&related=false', 'projects': 'listing?where={"style":"projects"}&sort=-publishedDate'}
    response = { "_endpoints": {}, 
                 "_links": { 
                            "self": { "href":"sections-latest", "title": "sections latest"}, 
                            "parent":{ "parend": "/", "title": "Home" } } }
    headers = dict(request.headers)
    tc = app.test_client()
    req = request.args.getlist('endpoint')
    for action in req:
        if action in endpoints:
            action_resp = tc.get(endpoints[action], headers=headers)
            headers = action_resp.headers
            action_data = json.loads(action_resp.data)
            if "_error" not in action_data and "_items" in action_data and len(action_data["_items"]) > 0:
                if action == 'choices':
                    response["_endpoints"][action] = {}
                    response["_endpoints"][action]['_items'] = action_data["_items"][0]["choices"]
                else:
                    response["_endpoints"][action] = action_data    
                for item in response["_endpoints"][action]["_items"]:
                    replace_imageurl(item)
    return Response(json.dumps(response), headers=headers)        

@app.route("/posts-alias", methods=['GET', 'POST'])
def get_posts_byname():
    allow_collections = ['sections', 'categories', 'tags', 'topics']
    headers = dict(request.headers)
    tc = app.test_client()
    collection = request.args.get('collection')
    name = request.args.get('name')
    content = request.args.get('content')
    if content == 'meta':
        endpoint = 'meta'
    else: 
        endpoint = 'posts'
    if collection in allow_collections:
        if collection == 'categories':
            table = 'postcategories'
        else:
            table = collection
        r = tc.get("/" + table + "/" + name, headers=headers)
        rs_data = json.loads(r.data)
        if "_error" not in rs_data and "_id" in rs_data:
            response = { "body": {} }
            collection_id = rs_data['_id']
            req = '/'+ endpoint + '?where={"' + collection + '":"' + collection_id + '"}'
            for key in dict(request.args):
                if key != 'collection' and key != 'name':
                    req += '&' + key + '=' + request.args.get(key)
            resp = tc.get(req, headers=headers)
            resp_data = json.loads(resp.data)
            for i in resp_data['_items']:
                replace_imageurl(i)
            return Response(json.dumps(resp_data), headers=resp.headers)  
        else:
            return r
    else:
        r = tc.get("/posts")
    return r

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
