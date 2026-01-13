pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/harshuasha/kubernetes_project_automotive_sensor_App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t your-dockerhub-harshuasha/flask-app:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }
}
