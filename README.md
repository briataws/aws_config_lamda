# REP: Raptor Event Processor (POC)

## Virtualenv

After cloning the repository:

    virtualenv .
    

Activate the virtual environment:

    source bin/activate
    

Install the pip dependencies:

    pip install -r requirements.txt
   

Json Schema CREATE

```
{"configurationItem": {"ARN": "arn:aws:ec2:us-east-1:605764505380:instance/i-059a7e3961b2dbb1f",
                         "availabilityZone": "us-east-1c",
                         "awsAccountId": "605764505380",
                         "awsRegion": "us-east-1",
                         "configuration": {"amiLaunchIndex": 0,
                                            "architecture": "x86_64",
                                            "blockDeviceMappings": [{"deviceName": "/dev/sda1",
                                                                      "ebs": {"attachTime": "2019-01-22T19:58:41.000Z",
                                                                               "deleteOnTermination": True,
                                                                               "status": "attached",
                                                                               "volumeId": "vol-0f2024169a6257e8b"}}],
                                            "capacityReservationId": None,
                                            "capacityReservationSpecification": {"capacityReservationPreference": "open",
                                                                                  "capacityReservationTarget": None},
                                            "clientToken": "",
                                            "cpuOptions": {"coreCount": 1,
                                                            "threadsPerCore": 1},
                                            "ebsOptimized": False,
                                            "elasticGpuAssociations": None,
                                            "enaSupport": True,
                                            "hypervisor": "xen",
                                            "iamInstanceProfile": None,
                                            "imageId": "ami-0ac019f4fcb7cb7e6",
                                            "instanceId": "i-059a7e3961b2dbb1f",
                                            "instanceLifecycle": None,
                                            "instanceType": "t2.micro",
                                            "kernelId": None,
                                            "keyName": "bcarpio",
                                            "launchTime": "2019-01-22T19:58:41.000Z",
                                            "monitoring": {"state": "disabled"},
                                            "networkInterfaces": [{"association": {"ipOwnerId": "amazon",
                                                                                     "publicDnsName": "ec2-54-205-104-127.compute-1.amazonaws.com",
                                                                                     "publicIp": "54.205.104.127"},
                                                                    "attachment": {"attachTime": "2019-01-22T19:58:41.000Z",
                                                                                    "attachmentId": "eni-attach-0e56f22e920b2a289",
                                                                                    "deleteOnTermination": True,
                                                                                    "deviceIndex": 0,
                                                                                    "status": "attached"},
                                                                    "description": "",
                                                                    "groups": [{"groupId": "sg-771cef36",
                                                                                 "groupName": "default"}],
                                                                    "ipv6Addresses": [],
                                                                    "macAddress": "12:71:18:81:59:6c",
                                                                    "networkInterfaceId": "eni-04d3a230d5d542f13",
                                                                    "ownerId": "605764505380",
                                                                    "privateDnsName": "ip-172-31-92-201.ec2.internal",
                                                                    "privateIpAddress": "172.31.92.201",
                                                                    "privateIpAddresses": [{"association": {"ipOwnerId": "amazon",
                                                                                                              "publicDnsName": "ec2-54-205-104-127.compute-1.amazonaws.com",
                                                                                                              "publicIp": "54.205.104.127"},
                                                                                             "primary": True,
                                                                                             "privateDnsName": "ip-172-31-92-201.ec2.internal",
                                                                                             "privateIpAddress": "172.31.92.201"}],
                                                                    "sourceDestCheck": True,
                                                                    "status": "in-use",
                                                                    "subnetId": "subnet-2a6cfd04",
                                                                    "vpcId": "vpc-bb8f29c1"}],
                                            "placement": {"affinity": None,
                                                           "availabilityZone": "us-east-1c",
                                                           "groupName": "",
                                                           "hostId": None,
                                                           "spreadDomain": None,
                                                           "tenancy": "default"},
                                            "platform": None,
                                            "privateDnsName": "ip-172-31-92-201.ec2.internal",
                                            "privateIpAddress": "172.31.92.201",
                                            "productCodes": [],
                                            "publicDnsName": "ec2-54-205-104-127.compute-1.amazonaws.com",
                                            "publicIpAddress": "54.205.104.127",
                                            "ramdiskId": None,
                                            "rootDeviceName": "/dev/sda1",
                                            "rootDeviceType": "ebs",
                                            "securityGroups": [{"groupId": "sg-771cef36",
                                                                 "groupName": "default"}],
                                            "sourceDestCheck": True,
                                            "spotInstanceRequestId": None,
                                            "sriovNetSupport": None,
                                            "state": {"code": 16,
                                                       "name": "running"},
                                            "stateReason": None,
                                            "stateTransitionReason": "",
                                            "subnetId": "subnet-2a6cfd04",
                                            "tags": [{"key": "ApplicationID",
                                                       "value": "39e02ab9dbd52b40711e54b8dc9619fc"},
                                                      {"key": "Name",
                                                       "value": "bcarpio-iop-test-16"}],
                                            "virtualizationType": "hvm",
                                            "vpcId": "vpc-bb8f29c1"},
                         "configurationItemCaptureTime": "2019-01-22T20:00:55.543Z",
                         "configurationItemStatus": "ResourceDiscovered",
                         "configurationItemVersion": "1.3",
                         "configurationStateId": 1548187255543,
                         "configurationStateMd5Hash": "",
                         "relatedEvents": [],
                         "relationships": [{"name": "Contains NetworkInterface",
                                             "resourceId": "eni-04d3a230d5d542f13",
                                             "resourceName": None,
                                             "resourceType": "AWS::EC2::NetworkInterface"},
                                            {"name": "Is associated with SecurityGroup",
                                             "resourceId": "sg-771cef36",
                                             "resourceName": None,
                                             "resourceType": "AWS::EC2::SecurityGroup"},
                                            {"name": "Is contained in Subnet",
                                             "resourceId": "subnet-2a6cfd04",
                                             "resourceName": None,
                                             "resourceType": "AWS::EC2::Subnet"},
                                            {"name": "Is attached to Volume",
                                             "resourceId": "vol-0f2024169a6257e8b",
                                             "resourceName": None,
                                             "resourceType": "AWS::EC2::Volume"},
                                            {"name": "Is contained in Vpc",
                                             "resourceId": "vpc-bb8f29c1",
                                             "resourceName": None,
                                             "resourceType": "AWS::EC2::VPC"}],
                         "resourceCreationTime": "2019-01-22T19:58:41.000Z",
                         "resourceId": "i-059a7e3961b2dbb1f",
                         "resourceName": None,
                         "resourceType": "AWS::EC2::Instance",
                         "supplementaryConfiguration": {},
                         "tags": {"ApplicationID": "39e02ab9dbd52b40711e54b8dc9619fc",
                                   "Name": "bcarpio-iop-test-16"}},
  "configurationItemDiff": {"changeType": "CREATE",
                             "changedProperties": {}},
  "messageType": "ConfigurationItemChangeNotification",
  "notificationCreationTime": "2019-01-22T20:00:56.499Z",
  "recordVersion": "1.3"}
```

Json Schema - DELETE

```
{'configrationItem': {'ARN': 'arn:aws:ec2:s-east-1:605764505380:instance/i-059a7e3961b2dbb1f',
                         'availabilityZone': None,
                         'awsAccontId': '605764505380',
                         'awsRegion': 's-east-1',
                         'configration': None,
                         'configrationItemCaptreTime': '2019-01-22T21:43:10.524Z',
                         'configrationItemStats': 'ResorceDeleted',
                         'configrationItemVersion': '1.3',
                         'configrationStateId': 1548193390524,
                         'configrationStateMd5Hash': '',
                         'relatedEvents': [],
                         'relationships': [],
                         'resorceCreationTime': None,
                         'resorceId': 'i-059a7e3961b2dbb1f',
                         'resorceName': None,
                         'resorceType': 'AWS::EC2::Instance',
                         'spplementaryConfigration': {},
                         'tags': {}},
  'configrationItemDiff': {'changeType': 'DELETE',
                             'changedProperties': {'Configration': {'changeType': 'DELETE',
                                                                       'previosVale': {'amiLanchIndex': 0,
                                                                                          'architectre': 'x86_64',
                                                                                          'blockDeviceMappings': [{'deviceName': '/dev/sda1',
                                                                                                                    'ebs': {'attachTime': '2019-01-22T19:58:41.000Z',
                                                                                                                             'deleteOnTermination': Tre,
                                                                                                                             'stats': 'attached',
                                                                                                                             'volmeId': 'vol-0f2024169a6257e8b'}}],
                                                                                          'capacityReservationId': None,
                                                                                          'capacityReservationSpecification': {'capacityReservationPreference': 'open',
                                                                                                                                'capacityReservationTarget': None},
                                                                                          'clientToken': '',
                                                                                          'cpOptions': {'coreCont': 1,
                                                                                                          'threadsPerCore': 1},
                                                                                          'ebsOptimized': False,
                                                                                          'elasticGpAssociations': None,
                                                                                          'enaSpport': Tre,
                                                                                          'hypervisor': 'xen',
                                                                                          'iamInstanceProfile': None,
                                                                                          'imageId': 'ami-0ac019f4fcb7cb7e6',
                                                                                          'instanceId': 'i-059a7e3961b2dbb1f',
                                                                                          'instanceLifecycle': None,
                                                                                          'instanceType': 't2.micro',
                                                                                          'kernelId': None,
                                                                                          'keyName': 'bcarpio',
                                                                                          'lanchTime': '2019-01-22T19:58:41.000Z',
                                                                                          'monitoring': {'state': 'disabled'},
                                                                                          'networkInterfaces': [{'association': {'ipOwnerId': 'amazon',
                                                                                                                                   'pblicDnsName': 'ec2-54-205-104-127.compte-1.amazonaws.com',
                                                                                                                                   'pblicIp': '54.205.104.127'},
                                                                                                                  'attachment': {'attachTime': '2019-01-22T19:58:41.000Z',
                                                                                                                                  'attachmentId': 'eni-attach-0e56f22e920b2a289',
                                                                                                                                  'deleteOnTermination': Tre,
                                                                                                                                  'deviceIndex': 0,
                                                                                                                                  'stats': 'attached'},
                                                                                                                  'description': '',
                                                                                                                  'grops': [{'gropId': 'sg-771cef36',
                                                                                                                               'gropName': 'defalt'}],
                                                                                                                  'ipv6Addresses': [],
                                                                                                                  'macAddress': '12:71:18:81:59:6c',
                                                                                                                  'networkInterfaceId': 'eni-04d3a230d5d542f13',
                                                                                                                  'ownerId': '605764505380',
                                                                                                                  'privateDnsName': 'ip-172-31-92-201.ec2.internal',
                                                                                                                  'privateIpAddress': '172.31.92.201',
                                                                                                                  'privateIpAddresses': [{'association': {'ipOwnerId': 'amazon',
                                                                                                                                                            'pblicDnsName': 'ec2-54-205-104-127.compte-1.amazonaws.com',
                                                                                                                                                            'pblicIp': '54.205.104.127'},
                                                                                                                                           'primary': Tre,
                                                                                                                                           'privateDnsName': 'ip-172-31-92-201.ec2.internal',
                                                                                                                                           'privateIpAddress': '172.31.92.201'}],
                                                                                                                  'sorceDestCheck': Tre,
                                                                                                                  'stats': 'in-se',
                                                                                                                  'sbnetId': 'sbnet-2a6cfd04',
                                                                                                                  'vpcId': 'vpc-bb8f29c1'}],
                                                                                          'placement': {'affinity': None,
                                                                                                         'availabilityZone': 's-east-1c',
                                                                                                         'gropName': '',
                                                                                                         'hostId': None,
                                                                                                         'spreadDomain': None,
                                                                                                         'tenancy': 'defalt'},
                                                                                          'platform': None,
                                                                                          'privateDnsName': 'ip-172-31-92-201.ec2.internal',
                                                                                          'privateIpAddress': '172.31.92.201',
                                                                                          'prodctCodes': [],
                                                                                          'pblicDnsName': 'ec2-54-205-104-127.compte-1.amazonaws.com',
                                                                                          'pblicIpAddress': '54.205.104.127',
                                                                                          'ramdiskId': None,
                                                                                          'rootDeviceName': '/dev/sda1',
                                                                                          'rootDeviceType': 'ebs',
                                                                                          'secrityGrops': [{'gropId': 'sg-771cef36',
                                                                                                               'gropName': 'defalt'}],
                                                                                          'sorceDestCheck': Tre,
                                                                                          'spotInstanceReqestId': None,
                                                                                          'sriovNetSpport': None,
                                                                                          'state': {'code': 16,
                                                                                                     'name': 'rnning'},
                                                                                          'stateReason': None,
                                                                                          'stateTransitionReason': '',
                                                                                          'sbnetId': 'sbnet-2a6cfd04',
                                                                                          'tags': [{'key': 'ApplicationID',
                                                                                                     'vale': '39e02ab9dbd52b40711e54b8dc9619fc'},
                                                                                                    {'key': 'Name',
                                                                                                     'vale': 'bcarpio-iop-test-16'}],
                                                                                          'virtalizationType': 'hvm',
                                                                                          'vpcId': 'vpc-bb8f29c1'},
                                                                       'pdatedVale': None},
                                                    'Relationships.0': {'changeType': 'DELETE',
                                                                         'previosVale': {'name': 'Is associated with SecrityGrop',
                                                                                            'resorceId': 'sg-771cef36',
                                                                                            'resorceName': None,
                                                                                            'resorceType': 'AWS::EC2::SecrityGrop'},
                                                                         'pdatedVale': None},
                                                    'Relationships.1': {'changeType': 'DELETE',
                                                                         'previosVale': {'name': 'Is attached to Volme',
                                                                                            'resorceId': 'vol-0f2024169a6257e8b',
                                                                                            'resorceName': None,
                                                                                            'resorceType': 'AWS::EC2::Volme'},
                                                                         'pdatedVale': None},
                                                    'Relationships.2': {'changeType': 'DELETE',
                                                                         'previosVale': {'name': 'Is contained in Sbnet',
                                                                                            'resorceId': 'sbnet-2a6cfd04',
                                                                                            'resorceName': None,
                                                                                            'resorceType': 'AWS::EC2::Sbnet'},
                                                                         'pdatedVale': None},
                                                    'Relationships.3': {'changeType': 'DELETE',
                                                                         'previosVale': {'name': 'Is contained in Vpc',
                                                                                            'resorceId': 'vpc-bb8f29c1',
                                                                                            'resorceName': None,
                                                                                            'resorceType': 'AWS::EC2::VPC'},
                                                                         'pdatedVale': None},
                                                    'Relationships.4': {'changeType': 'DELETE',
                                                                         'previosVale': {'name': 'Contains NetworkInterface',
                                                                                            'resorceId': 'eni-04d3a230d5d542f13',
                                                                                            'resorceName': None,
                                                                                            'resorceType': 'AWS::EC2::NetworkInterface'},
                                                                         'pdatedVale': None}}},
  'messageType': 'ConfigrationItemChangeNotification',
  'notificationCreationTime': '2019-01-22T21:43:11.322Z',
  'recordVersion': '1.3'}
```