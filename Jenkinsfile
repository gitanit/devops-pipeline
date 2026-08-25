pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                echo 'Running application test...'

                sh '''
                    echo "Preparing test context..."

                    rm -rf /build-context/*

                    cp application.py /build-context/
                    cp test_application.py /build-context/

                    echo "Test context:"
                    ls -la /build-context

                    echo "Running Python application..."

                    podman run --rm \
                        -v /home/shahariaranit/podman-build-context:/app \
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
                    echo "Preparing Docker build context..."

                    cp Dockerfile /build-context/

                    echo "Build context:"
                    ls -la /build-context

                    echo "Building image..."

                    podman build \
                        -t devops-pipeline:${BUILD_NUMBER} \
                        /home/shahariaranit/podman-build-context
                '''
            }
        }

        stage('Verify Image') {
            steps {
                echo 'Verifying container image...'

                sh '''
                    echo "Available devops-pipeline images:"

                    podman images | grep devops-pipeline
                '''
            }
        }
    }

    post {
        success {
            echo '======================================'
            echo 'CI PIPELINE COMPLETED SUCCESSFULLY!'
            echo '======================================'
        }

        failure {
            echo '======================================'
            echo 'CI PIPELINE FAILED'
            echo 'Check the stage above for the error.'
            echo '======================================'
        }
    }
}
