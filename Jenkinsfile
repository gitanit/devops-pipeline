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
                        -v /home/shahariaranit/.local/share/containers/storage/volumes/jenkins_home/_data/workspace/devops-pipeline:/app \
                        -w /app \
                        python:3.12-alpine \
                        python3 application.py
                '''
            }
        }

        stage('Build Image') {
            steps {
                echo 'Preparing build context...'

                sh '''
                    rm -rf /build-context/*
                    cp -r "$WORKSPACE"/. /build-context/
                '''

                echo 'Building container image...'

                sh '''
                    podman build \
                        -t devops-pipeline:${BUILD_NUMBER} \
                        /build-context
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
