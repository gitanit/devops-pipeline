pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'Running application test...'

                sh '''
                    podman run --rm \
                        -v "$PWD:/app:Z" \
                        -w /app \
                        python:3.12-alpine \
                        python3 application.py
                '''
            }
        }

        stage('Build Image') {
            steps {
                echo 'Building container image...'

                sh '''
                    podman build \
                        -t devops-pipeline:${BUILD_NUMBER} \
                        .
                '''
            }
        }

        stage('Verify Image') {
            steps {
                sh 'podman images | grep devops-pipeline'
            }
        }
    }
}
