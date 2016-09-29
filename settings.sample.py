# MONGO DATABASE SETTINGS
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'keystone-test'
ASSETS_URL = 'http://stage.mirrormedia.mg/'
GCS_URL = 'https://storage.googleapis.com/mirrormedia-dev/'

# ALLOW ACTIONS
DEBUG = False
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE'] if DEBUG else ['GET']

meta_schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'sections': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'sections',
      'field': '_id',
      'embeddable': True
    },
  },
  'topics': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'topics',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'isAdvertised': {
    'type': 'boolean',
  },
  'publishedDate': {
    'type': 'string',
  },
  'og_description': {
    'type': 'string',
  },
}

post_schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'state': {
    'type': 'string',
  },
  'sections': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'sections',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'writers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'photographers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'designers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'engineers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'publishedDate': {
    'type': 'string',
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'topics': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'topics',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  #'topics_ref': {
  #  'type': 'list',
  #  'schema': {
  #      'type': 'objectid',
  #      'data_relation': {
  #          'resource': 'meta',
  #          'field': 'topics',
  #          'embeddable': True
  #       },
  #   },
  #},
  'tags': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'tags',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'style': {
    'type': 'string',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'content': {
    'type': 'dict',
    'schema': {
       "html": {
          "type": "string",
       },
     },  
  },
  'relateds': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
  'extend_byline': {
    'type': 'string',
  },
  'og_title': {
    'type': 'string',
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'isAdvertised': {
    'type': 'boolean',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  }
}

user_schema = {
  'name': {
    'type': 'string',
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
  },
  'role': {
    'type': 'string',
  },
  'company': {
    'type': 'string',
  },
  'address': {
    'type': 'string',
  }
}

contact_schema = {
  'name': {
    'type': 'string',
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  },
  'homepage': {
    'type': 'string',
  },
  'facebook': {
    'type': 'string',
  },
  'twitter': {
    'type': 'string',
  },
  'instantgram': {
    'type': 'string',
  },
  'bio': {
    'type': 'string',
  },
  'image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
}

member_schema = {
  'member_id': {
    'type': 'string',
    'required': True,
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
  },
  'password': {
    'type': 'string',
    'required': True,
  },
  'country': {
    'type': 'string',
  },
  'city': {
    'type': 'string',
  },
  'address': {
    'type': 'string',
  },
  'zip': {
    'type': 'interger',
  },
  'gender': {
    'type': 'string',
  },
  'state': {
      'type': 'dict',
      'schema': {
          'bookmark': {
            'type': 'list',
            'schema': {
              'type': 'objectid',
              'data_relation': {
                'resource': 'posts',
                'field': '_id',
                'embeddabole': True
              },
            },
          },
          'bookmark_count': {
            'type': 'integer',
          },
          'position': {
            'type': 'string',
          }
      },
  },
  'create_date': {
    'type': 'datetime',
  }
}

postcategories_schema = {
    'name': {
      'type': 'string',
    },
    'title': {
      'type': 'string',
    }
}


sections_schema = {
    'title': {
      'type': 'string',
    },
    'name': {
      'type': 'string',
    },
    'type': {
      'type': 'string',
      'allowed': ['articles', 'file', 'link']
    },
    'description': {
      'type': 'string',
    },
    'image': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'images',
        'field': '_id',
        'embeddable': True
      },
    },
    'categories': {
      'type': 'list',
      'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
       },
    },
    'style': {
      'type': 'string',
    }
}

account_schema = {
    'username': {
       'type': 'string',
       'required': True,
       'unique': True,
    },
    'password': {
       'type': 'string',
       'required': True,
    },
    'roles': {
        'type': 'list',
        'allowed': ['user', 'superuser', 'admin'],
        'required': True,
    },
    'token': {
        'type': 'string',
        'required': True,
    }
}

videos_schema = {
  'description': {
    'type': 'string',
  },
  'video': {
    'type': 'dict',
    'schema': {
        'filetype': {
          'type': 'string',
        },
        'filename': {
          'type': 'string',
        },
        'originalname': {
          'type': 'string',
        },
        'path': {
          'type': 'string',
        },
        'projectId': {
          'type': 'string',
        },
        'size': {
          'type': 'string',
        },
        'url': {
          'type': 'string',
        },
    },
  },  
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
}

audios_schema = {
  'description': {
    'type': 'string',
  },
  'audio': {
    'type': 'dict',
    'schema': {
        'filetype': {
          'type': 'string',
        },
        'filename': {
          'type': 'string',
        },
        'originalname': {
          'type': 'string',
        },
        'path': {
          'type': 'string',
        },
        'projectId': {
          'type': 'string',
        },
        'size': {
          'type': 'string',
        },
        'url': {
          'type': 'string',
        },
    },
  },  
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
}

topics_schema = {
  'name': {
    'type': 'string',
  }
}

choices_schema = {
  'pickDate': {
    'type': 'string',
  },
  'choices': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
}

image_schema = {
  'photographer': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'contacts',
      'field': '_id',
      'embeddable': True
    },
  },
  'description': {
    'type': 'string',
  },
  'sale': {
    'type': 'Boolean',
  },
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
  'image': {
    'type': 'dict',
    'schema': {
      'artist': {
        'type': 'string',
      },
      'description': {
        'type': 'string',
      },
      'filename': {
        'type': 'string',
      },
      'filetype': {
        'type': 'string',
      },
      'height': {
        'type': 'number',
      },
      'width': {
        'type': 'number',
      },
      'size': {
        'type': 'number',
      },
      'url': {
        'type': 'string',
      }
    },
  },
}

posts = {
    'item_title': 'post',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['writers','photographers','designers','engineers','heroImage', 'topics', 'sections', 'categories', 'tags'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': post_schema
}

meta = {
    'item_title': 'draft',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage','writers', 'topics','sections', 'categories'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': meta_schema
}
drafts = {
    'item_title': 'draft',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'draft'},
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': post_schema
}

users = {
    'item_title': 'user',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=60,must-revalidate',
    'cache_expires': 60,
    'allow_unknown': False,
    'schema': user_schema
}

members = {
    'item_title': 'member',
    'additional_lookup': {
        'url': 'regex("\w+")',
        'field': 'member_id'
    },
    'resource_methods': ['GET', 'POST'],
    'cache_control': 'max-age=60,must-revalidate',
    'cache_expires': 60,
    'allow_unknown': False,
    'schema': member_schema
}

contacts = {
    'item_title': 'contact',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'embedded_fields': ['image'],
    'schema': contact_schema
}

choices = {
    'item_title': 'choice',
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': choices_schema
}

topics = {
    'item_title': 'topic',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': topics_schema
}

tags = {
    'item_title': 'tag',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': {
      'name': {
        'type': 'string',
      }
    }
}

postcategories = {
    'item_title': 'postcategory',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': postcategories_schema,
}

sections = {
    'item_title': 'section',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['categories', 'image'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'allow_unknown': False,
    'schema': sections_schema,
}

account = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },
    'resource_methods': ['GET', 'POST'],
    'allowed_roles': ['superuser', 'admin'],
    'cache_control': '',
    'cache_expires': 0,
    'schema': account_schema,
}

images = {
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'schema': image_schema,
}

audios = {
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'schema': audios_schema,
}

videos = {
    'resource_methods': ['GET'],
    'cache_control': 'max-age=300,must-revalidate',
    'cache_expires': 300,
    'schema': videos_schema,
}

DOMAIN = {
    'posts': posts,
    'drafts': drafts,
    'meta': meta,
    'users': users,
    'members': members,
    'contacts': contacts,
    'tags': tags,
    'choices': choices,
    'topics': topics,
    'postcategories': postcategories,
    'account': account,
    'images': images,
    'audios': audios,
    'videos': videos,
    'sections': sections,
    }

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
