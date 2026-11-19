pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}/.python-packages"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    mkdir -p "$WORKSPACE/.python-packages"
                    python3 -m pip install --target "$WORKSPACE/.python-packages" Flask==3.1.1
                    python3 -c "import flask; print('Flask installed successfully:', flask.__version__)"
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
                    mkdir -p "$WORKSPACE/python-app-deploy"
                    cp app.py "$WORKSPACE/python-app-deploy/"
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application...'
                sh '''
                    nohup python3 "$WORKSPACE/python-app-deploy/app.py" > "$WORKSPACE/python-app-deploy/app.log" 2>&1 < /dev/null &
                    echo $! > "$WORKSPACE/python-app-deploy/app.pid"
                    sleep 2
                '''
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing application...'
                sh 'python3 test_app.py'
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
