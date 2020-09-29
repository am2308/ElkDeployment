pipeline {
  agent any 
  stages {
    stage('Deploy ELK stack in kubernetes') {
      steps {
        sh """
        cd /root/ElkDeploy/${params.env}/${params.version}
        ls -lart
        ansible-playbook deployment.yaml -i hosts/groups
        """
      }
    }
    stage('Run kubectl command to versify the deployment') {
      steps {
        sh """
        cd /root/ElkDeploy/${params.env}/${params.version}
        sleep 60s
        kubectl get pods --insecure-skip-tls-verify -o wide
        kubectl get services --insecure-skip-tls-verify -o wide
        kubectl get configmaps --insecure-skip-tls-verify -o wide
        kubectl get deploy --insecure-skip-tls-verify
        """
      }
    }
  }
}
