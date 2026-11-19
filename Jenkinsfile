pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Checking Python and Flask...'
                sh '''
                    python3 --version
                    python3 -c "import sys; sys.path.insert(0, '/var/jenkins_home/python-packages'); import flask; print('Flask:', flask.__version__)"
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
