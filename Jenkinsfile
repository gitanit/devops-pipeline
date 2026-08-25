pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python3 --version'
                sh 'python3 application.py'
            }
        }

        stage('Build Image') {
            steps {
                sh 'podman build -t devops-pipeline:${BUILD_NUMBER} .'
            }
        }

    }
}
