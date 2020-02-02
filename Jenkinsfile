pipeline {
    agent none

    environment {
	    PYTHONUNBUFFERED = 1
    }

    stages {
	stage('pull') {
	    agent any
	    steps {
		    sh '$(pwd)/pull'
	    }
	}
	stage('build') {
	    agent { docker { image 'python:3.6-alpine' } }
	    steps {
		    sh 'pip install -r requirements.txt'
		    sh 'python app/manage.py migrate'
	    }
	}
	stage('test') {
	    agent { docker { image 'python:3.6-alpine' } }
	    steps {
		    sh 'python app/manage.py test app'
	    }
	}
	stage('deploy') {
	    agent any
	    steps {
		sh '$(pwd)/deploy'
	    }
	}
    }

    post {
        always {
            echo 'Stages Completed!'
        }
        success {
            echo 'Passed! Deploying Changes...'
        }
        failure {
            echo 'Failed! Ignoring Changes...'
        }
    }
}

// TODO: SAVE THE LATEST SUCCESSFUL BUILD CODES AND RELOAD IN CASE OF 'failure'