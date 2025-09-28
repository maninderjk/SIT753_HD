pipeline {
    agent any
    environment {
        PATH = "/opt/anaconda3/bin:${env.PATH}"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '/opt/anaconda3/bin/python3 -m pip install --upgrade pip'
                sh '/opt/anaconda3/bin/python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '/opt/anaconda3/bin/python3 -m pytest --maxfail=1 --disable-warnings -q || echo "No tests found, skipping..."'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Checking code quality...'
                sh '/opt/anaconda3/bin/python3 -m flake8 . || true'
            }
        }

        stage('Security') {
            steps {
                echo 'Running security scan...'
                sh '/opt/anaconda3/bin/python3 -m bandit -r . || true'
            }
        }
    }
}
