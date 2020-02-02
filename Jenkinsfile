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
        stage('build and test')
        {
            agent
            {
                dockerfile true
            }

            steps
            {
                sh 'python app/manage.py migrate'
                sh 'python app/manage.py test app'
            }
        }
        stage('deploy')
        {
            agent any
            steps
            {
                sh 'pwd'
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