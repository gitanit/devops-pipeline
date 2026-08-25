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
                        -v "$PWD:/app" \
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

                    cp Dockerfile /build-context/
                    cp application.py /build-context/
                    cp test_application.py /build-context/

                    echo "Build context:"
                    ls -la /build-context

                    echo "Building container image..."

                    podman build \
                        -t devops-pipeline:${BUILD_NUMBER} \
                        /build-context
                '''
            }
        }

        stage('Verify Image') {
            steps {
                echo 'Verifying image...'

                sh '''
                    podman images | grep devops-pipeline
                '''
            }
        }
    }
}
