pipeline {
  agent any

  stages {
    stage("Delete Old Container") {
      steps {
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          echo "Deleting old container"
          sh "docker rm -f my-python-app"
        }
      }
    }

    stage("Building and Running Container") {
      steps {
        echo "Building and running container"
        sh "docker build -t my-python-app ."
        sh "docker run -d --name my-python-app my-python-app"
      }
    }

    stage("Testing") {
      steps {
        echo "Running tests"
        sh "docker exec my-python-app pytest /app/tests/test_math.py"
      }
    }

    stage("Deploy") {
      steps {
        echo "Deployment process"
        # Add deployment steps here
      }
    }
  }

  post {
    always {
      echo "Cleaning up"
      sh "docker stop my-python-app"
      sh "docker rm my-python-app"
    }

    failure {
      echo "Oh no, the pipeline failed!"
    }

    success {
      echo "Yay, the pipeline succeeded!"
    }
  }
}

