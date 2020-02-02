pipeline
{
    agent none

    environment
    {
	    PYTHONUNBUFFERED = 1
    }

    stages
    {
        stage('pull')
        {
            agent any
            steps
            {
                sh '$(pwd)/pull'
            }
        }
        stage('build')
        {
            agent
            {
                dockerfile true
            }

            steps
            {
                sh 'python app/manage.py migrate'
            }
        }
        stage('test')
        {
            agent
            {
                dockerfile true
            }
            steps
            {
                sh 'python app/manage.py test app'
            }
        }
        stage('deploy')
        {
            agent any
            steps
            {
                sg 'echo $(who am I)'
                sh '$(pwd)/deploy'
            }
        }
    }

    post
    {
        always
        {
            echo 'Stages Completed!'
        }
        success
        {
            echo 'Passed! Deploying Changes...'
        }
        failure
        {
            echo 'Failed! Ignoring Changes...'
        }
    }
}

// TODO: SAVE THE LATEST SUCCESSFUL BUILD CODES AND RELOAD IN CASE OF 'failure'