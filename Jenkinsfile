pipeline {
    agent any

    environment {
        BUILD_CONTEXT = "/build-context"
        IMAGE_NAME = "devops-pipeline"
    }

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
                    set -e

                    echo "Preparing test context..."

                    rm -f ${BUILD_CONTEXT}/application.py
                    rm -f ${BUILD_CONTEXT}/test_application.py

                    cp application.py ${BUILD_CONTEXT}/
                    cp test_application.py ${BUILD_CONTEXT}/

                    echo "Test context:"
                    ls -la ${BUILD_CONTEXT}

                    echo "Running Python application..."

                    podman run --rm \
                        -v ${BUILD_CONTEXT}:/app \
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
                    set -e

                    echo "Preparing Docker build context..."

                    cp Dockerfile ${BUILD_CONTEXT}/

                    echo "Build context:"
                    ls -la ${BUILD_CONTEXT}

                    echo "Building image..."

                    podman build \
                        -t ${IMAGE_NAME}:${BUILD_NUMBER} \
                        ${BUILD_CONTEXT}
                '''
            }
        }

        stage('Verify Image') {
            steps {
                echo 'Verifying built image...'

                sh '''
                    set -e

                    podman images

                    podman image inspect \
                        ${IMAGE_NAME}:${BUILD_NUMBER} \
                        > /dev/null

                    echo "======================================"
                    echo "IMAGE BUILD SUCCESSFUL"
                    echo "Image: ${IMAGE_NAME}:${BUILD_NUMBER}"
                    echo "======================================"
                '''
            }
        }
    }

    post {
        success {
            echo '''
======================================
CI PIPELINE SUCCESSFUL
======================================
'''
        }

        failure {
            echo '''
======================================
CI PIPELINE FAILED
======================================
Check the stage above for the error.
'''
        }
    }
}
