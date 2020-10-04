pipeline {
  agent any 
  stages {
    stage('Geting controller ip and creating host file') {
      steps {
        sh """
        cd /root/ElkDeploy/${params.env}/${params.version}
        chmod 755 GetControllerIp.py
        python GetControllerIp.py ${params.Region}
        mv -f groups hosts/groups
        """
      }
    }
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
        sleep 10s
        kubectl get pods --insecure-skip-tls-verify -o wide
        kubectl get services --insecure-skip-tls-verify -o wide
        kubectl get configmaps --insecure-skip-tls-verify -o wide
        kubectl get deploy --insecure-skip-tls-verify
        kubectl get daemonsets --insecure-skip-tls-verify -o wide
        """
      }
    }
  }
}
