pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('test') {
            steps {
                sh 'pytest tests'
            }
        }
        stage('build and run') {
            steps {
                sh 'docker-compose up -d --build && docker-compose up'
            }
        }
    }
}

