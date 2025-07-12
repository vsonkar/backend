pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning backend repo and preparing environment...'
            }
        }

        stage('Run App') {
            steps {
                echo 'Simulating Flask app start...'
                // You can later replace this with:
                // sh 'python3 app.py' or bat 'python app.py'
            }
        }
    }
}
