pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh '''
                    set -eu

                    rm -rf .venv
                    /usr/bin/python3 -m venv --without-pip .venv

                    SITE="$WORKSPACE/.venv/lib/python3.13/site-packages"
                    mkdir -p "$SITE"

                    echo "Copying Flask and its dependencies..."

                    for package in flask blinker click itsdangerous jinja2 markupsafe werkzeug; do
                        find /usr/lib/python3/dist-packages \
                            -maxdepth 1 \
                            \\( -name "$package" \
                            -o -name "$package-*.dist-info" \
                            -o -name "$package-*.egg-info" \\) \
                            -exec cp -a {} "$SITE/" \\;
                    done

                    echo "Verifying Flask..."
                    .venv/bin/python -c "import flask; print('Flask:', flask.__file__); print('Version:', flask.__version__)"

                    echo "Build completed."
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
                    echo "Deployment contents:"
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
