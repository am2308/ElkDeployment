#/bin/python

import sys
import boto3
Region = str(sys.argv[1])

#This will create a client of aws ec2 for the specified region
ec2 = boto3.client('ec2', region_name=Region)
#InstanceList = ['etcd-0', 'controller-0', 'worker-0', 'worker-1', 'worker-2']
data = ""
#Above created client will interect with ec2 instances using AWS SDKs based upon filtered instances
response = ec2.describe_instances()


#This is the sample attribute that you can fetch, I have fetched "PublicIp" for worker nodes, etcd, controller and created host file for ansible


for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        for tags in instance['Tags']:
                if tags['Key'] == 'Name' and tags['Value'].startswith('cont') and instance['State']['Name'] == "running":
                        if tags['Value'].startswith('cont'):
                                data = data + "[controller]\ncontroller ansible_ssh_host=" + instance['PublicIpAddress'] + "\n"
                elif tags['Key'] == 'Name' and tags['Value'] == "worker-0" and instance['State']['Name'] == "running":
                        data = data + "[worker]\nworker ansible_ssh_host=" + instance['PublicIpAddress'] + "\n"



f = open('groups' ,'w')
f.write(data)
f.close()
