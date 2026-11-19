pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing Flask dependencies...'
                sh '''
                    mkdir -p "$WORKSPACE/.python-packages"

                    PYTHONPATH=/usr/lib/python3/dist-packages \
                    python3 -m pip install \
                    --break-system-packages \
                    --target "$WORKSPACE/.python-packages" \
                    -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    PYTHONPATH="$WORKSPACE/.python-packages:/usr/lib/python3/dist-packages" \
                    python3 -m unittest discover -s .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    rm -rf "$WORKSPACE/python-app-deploy"
                    mkdir -p "$WORKSPACE/python-app-deploy"

                    cp app.py requirements.txt "$WORKSPACE/python-app-deploy/"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
