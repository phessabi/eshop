pipeline
{
    agent none

    environment
    {
	    PYTHONUNBUFFERED = 1
	    PRODUCT_PATH = '/home/ubuntu/eshop'
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
				sh 'python app/manage.py check --deploy'
				
            }
        }
        stage('deploy')
        {
            agent any
            steps
            {
                sh '$(pwd)/deploy ${PRODUCT_PATH}'
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

