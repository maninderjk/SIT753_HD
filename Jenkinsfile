pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '/opt/anaconda3/bin/python3 -m pip install --upgrade pip'
                sh '/opt/anaconda3/bin/python3 -m pip install -r requirements.txt'
            }
        }


        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Code Quality') {
            steps {
                echo "Running flake8 linting..."
                sh 'flake8 . || true'
            }
        }

        stage('Security') {
            steps {
                echo "Running Bandit security scan..."
                sh 'bandit -r . || true'
            }
        }
    }
}
