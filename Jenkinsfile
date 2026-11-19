pipeline {
    agent any

    environment {
        PYTHON = '/var/jenkins_home/flask-venv/bin/python'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh '''
                    "$PYTHON" --version
                    "$PYTHON" -c "import flask; print('Flask installed:', flask.__version__)"
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '"$PYTHON" -m unittest discover -s .'
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
