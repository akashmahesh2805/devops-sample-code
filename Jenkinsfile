
pipeline {
    agent any

    environment {
        VENV = "/tmp/flask-jenkins-venv"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                sh '''
                    rm -rf "$VENV"
                    python3 -m venv "$VENV"
                    "$VENV/bin/pip" install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '"$VENV/bin/python" -m unittest discover -s .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    mkdir -p "$WORKSPACE/python-app-deploy"
                    cp "$WORKSPACE/app.py" "$WORKSPACE/python-app-deploy/"
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application...'
                sh '''
                    nohup "$VENV/bin/python" "$WORKSPACE/python-app-deploy/app.py" > "$WORKSPACE/python-app-deploy/app.log" 2>&1 &
                    echo $! > "$WORKSPACE/python-app-deploy/app.pid"
                '''
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing application...'
                sh '"$VENV/bin/python" test_app.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}
