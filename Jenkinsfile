pipeline {
    agent any

    environment {
        PYTHONPATH = '/var/jenkins_home/python-packages'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh '''
                    python3 --version
                    python3 -c "import flask; print('Flask installed:', flask.__version__)"
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest discover -s .'
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
