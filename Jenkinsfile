pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh '''
                    set -e

                    echo "Checking Python version..."
                    /usr/bin/python3 --version

                    echo "Checking Flask dependency..."
                    /usr/bin/python3 -c "import flask; print('Flask version:', flask.__version__)"

                    echo "Checking application syntax..."
                    /usr/bin/python3 -m py_compile app.py test_app.py

                    echo "Build completed successfully."
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    set -e
                    /usr/bin/python3 -m unittest discover -s . -p 'test_*.py' -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Python application...'
                sh '''
                    set -e

                    rm -rf python-app-deploy
                    mkdir -p python-app-deploy

                    cp app.py requirements.txt python-app-deploy/

                    echo "Deployment contents:"
                    ls -l python-app-deploy/

                    echo "Deployment completed successfully."
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
