pipeline {
    agent {docker {image 'python:3.7.2' }}

    stages {
        stage('Build') {
            steps {
                echo 'Hello testing world'
            }
        }
        stage('Test 1') {    
            steps { 
                
               withEnv(["HOME=${env.WORKSPACE}"]){
                sh 'pip install --user -r req.txt'
                sh 'python Assignment2_test_doubles.py'
              
                } 
               
            }
        }
        
        stage('Test 2') {
           steps {
                withEnv(["HOME=${env.WORKSPACE}"]){
          
                    
                sh """
                    pip3 install  --user docker-compose
                    ls
                    /var/jenkins_home/workspace/test/.local/bin/docker-compose version
                    /var/jenkins_home/workspace/test/.local/bin/docker-compose build
                    /var/jenkins_home/workspace/test/.local/bin/docker-compose up
                    """
                 
                }  
               
           }
       }
    }
}
