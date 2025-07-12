pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/vsonkar/backend'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'pm2 restart flask-app || pm2 start app.py --name flask-app'
            }
        }
    }
}
