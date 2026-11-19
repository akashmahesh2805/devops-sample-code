pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh '''
                    set -e
                    rm -rf .venv
                    python3 -m venv .venv
                    .venv/bin/python --version
                    .venv/bin/python -m pip install -r requirements.txt
                    .venv/bin/python -c "import flask; print('Flask installed:', flask.__version__)"
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    set -e
                    .venv/bin/python -m unittest discover -s . -p 'test_*.py' -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    set -e
                    rm -rf python-app-deploy
                    mkdir -p python-app-deploy
                    cp app.py requirements.txt python-app-deploy/
                    echo 'Application deployed to python-app-deploy/'
                    ls -l python-app-deploy/
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
