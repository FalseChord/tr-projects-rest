node {
    def project = 'mirrormedia-1470651750304'
    def appName = 'mirrormedia-rest'
    def imageTag = "gcr.io/${project}/${appName}"

    def build_time 
    def git_author_mail
    def git_author_name
    def slack_user

    stage('Pre-build Setup') {
        // checkout([$class: 'GitSCM', branches: [[name: '*/dev']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'AuthorInChangelog']], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/ichiaohsu/plate-vue']]])
        try {
            checkout scm
            
            git_author_mail = sh(
                script: "git log --skip 1 -n 1 --pretty=%aE",
                returnStdout: true
            ).trim()
            
            git_author_name = sh(
                script: "git log --skip 1 -n 1 --pretty=%an",
                returnStdout: true
            ).trim()

            sh("echo git pushed by ${git_author_name} ${git_author_mail}")

            slack_user = slackUsers(git_author_mail)
            sh("echo slack target: ${slack_user}")

            sh("git clone https://github.com/mirror-media/twreporter-restful-docker.git")

            sh("gcloud source repos clone default --project=mirrormedia-1470651750304")
            sh("cp default/tr-project-rest/settings.py twreporter-restful-docker/")
            
        } catch(e) {
            slackSend (color: '#FF0000', message: "Huston, we got a *pre-build* problem.")
            currentBuild.result = 'FAILURE'
            throw e
        }

        slackSend (color: '#C5C9CC', message: "*${git_author_name}* gave *${appName}* a little push. Let the build begin!")
    }
    
    stage('Build'){
        dir("./twreporter-restful-docker"){
            try {
                build_time = sh(
                    script: "date +%Y-%m-%d_%H%M%S",
                    returnStdout: true
                ).trim()
                // sh("date +%Y-%m-%d_%H%M%S > .finishtime")
                // build_time = readFile '.finishtime'
                sh("docker build --no-cache -t ${imageTag}:${slack_user}_${build_time} .")
                // sh("echo ${build_time}")
                
                sh("gcloud docker -- push ${imageTag}:${slack_user}_${build_time}")
            } catch(e) {
                slackSend (color: '#FF0000', message: "@${slack_user}, we got a *build* problem.")
                currentBuild.result = 'FAILURE'
                throw e
            }
            
            slackSend (color: '#BDFFC3', message: "Build ${slack_user}_${build_time} *SUCCESS*.\n Make NEWS great again!")
        }
    }

    stage("Deploy") {
        try {
            // Deploy to dev
            sh("kubectl set image deploy/rest-deployment mm-rest=${imageTag}:${slack_user}_${build_time}")
            // Watch until rollout success
            sh("kubectl rollout status deployment/rest-deployment -w")

            sh("sleep 30s")

        } catch(e) {
            slackSend (color: '#FF0000', message: "Huston, we got a *deploy* problem.")
            currentBuild.result = 'FAILURE'
            throw e
        }
        
        slackSend (color: '#FCE028', message: "@${slack_user}, take a *REST*. Check out new *DEPLOY* at https://dev.mirrormedia.mg")
    }
}

def slackUsers(git_email){
    switch(git_email){
        case "chiangkaichih@gmail.com":
            return "chiangkeith"
        case "lion15945@gmail.com":
            return "kwhsiung"
        case "hcchien@gmail.com":
            return "hcchien"
        case "tempo0829@gmail.com":
            return "noah.tan"
        case "ichiao.hsu@gmail.com":
            return "mmich"
        default:
            return "hcchien"
    }
}