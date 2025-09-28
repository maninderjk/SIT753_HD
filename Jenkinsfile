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
                echo "Building Docker image..."
                sh 'docker build -t flask-task-manager .'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests with pytest..."
                sh 'pip install -r requirements.txt'
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
