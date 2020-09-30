# Logging Infrastructure using ELK in Kubernetes

This is a sample setup for automated logging with the elastic stack on Kubernetes.

## It uses components :

* Elasticsearch for storing and searching logs.
* Kibana for viewing them.
* Logstash for analysing and breaking down logs.
* Filebeat for pushing all app logs to logstash.

## Requirements

- Kubernetes cluster (Already provisioned using Terraform and Ansible)
- Docker (Already installed)

## Components deployment types

Elasticsearch is installed as a StatefulSet so that there is some
awareness betwee them.

Filebeat is installed as DaemonSets, meaning there is one for every node we have. This is because they
read the logs right off the node. Without this we would miss logs from some nodes.

Logstash and Kibana are installed as simple deployments.

## Installation

We are deploying ELK stack in kubernetes cluster using ansible

```
$ ansible-playbook deployment.yaml
```
deployment.yaml internally deploying/creating statefulsets, configmaps, deployments and services using kubectl command.

## Kubectl commands used

This command will create statefulsets app along with service of type ClusterIp
```
$ kubectl apply -f elasticsearch.yaml
```
This command will create configmaps for filebeat
```
$ kubectl apply -f filebeatConfig.yaml
```
This command will create filebeat deployment
```
$ kubectl apply -f filebeat.yaml
```
This command will create configmaps for logstash
```
$ kubectl apply -f logstashConfig.yaml
```

This command will create deployment for logstash
```
$ kubectl apply -f logstash.yaml
```

This command will deployment and service of type NodePort for kibana
```
$ kubectl apply -f kibana.yaml
```

