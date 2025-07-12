pipeline {
    agent any

    tools {
        python 'Python3'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/vsonkar/backend'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Restart Flask App') {
            steps {
                sh 'pm2 restart flask-app || pm2 start app.py --name flask-app'
            }
        }
    }
}
