pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh '''
                    set -e

                    rm -rf .venv

                    /usr/bin/python3 -m venv --without-pip .venv

                    # Make Debian's installed Python packages visible
                    echo "/usr/lib/python3/dist-packages" > .venv/lib/python3.13/site-packages/debian-packages.pth

                    .venv/bin/python --version
                    .venv/bin/python -c "import flask; print('Flask installed:', flask.__version__)"

                    echo "Build completed successfully."
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
                    echo "Deployment completed successfully."
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
