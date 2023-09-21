import os, json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def write_message_to_sqs(event, context):
    message = event['Records'][0]['Sns']['Message']
    # logger.info('got event{}'. format(message))
    pmessage = json.loads(message)
    try:
        if (pmessage['configurationItem']['resourceType'] == 'AWS::EC2::Instance') and (pmessage['configurationItemDiff']['changeType'] in ('CREATE', 'UPDATE')):
            for tag in pmessage['configurationItem']['configuration']['tags']:
                if tag['key'] == 'ApplicationID':
                    client = boto3.client('sqs')
                    response = client.send_message(
                        QueueUrl = os.environ['QUEUE_URL'],
                        MessageAttributes={
                            'type': {
                                'DataType': 'String',
                                'StringValue': 'awsconfig_cmdb'
                            },
                            'published_by': {
                                'DataType': 'String',
                                'StringValue': 'lambda' # Make Dynamic
                            },
                            'source': {
                                'DataType': 'String',
                                'StringValue': 'aws'
                            },
                            'transaction_id': {
                                'DataType': 'String',
                                'StringValue': pmessage['configurationItem']['configurationStateId']
                            },
                            'origin': {
                                'DataType': 'String',
                                'StringValue': 'aws'
                            },
                            'changeType': {
                                'DataType': 'String',
                                'StringValue': pmessage['configurationItemDiff']['changeType']
                            },
                            'create_time': {
                                'DataType': 'String',
                                'StringValue': pmessage['notificationCreationTime']
                            },
                            'awsAccountId': {
                                'DataType': 'String',
                                'StringValue': pmessage['configurationItem']['awsAccountId']
                            }
                        },
                        MessageBody=json.dumps(pmessage)
                    )
                    return response

        elif (pmessage['configurationItem']['resourceType'] == 'AWS::EC2::Instance') and (pmessage['configurationItemDiff']['changeType'] == 'DELETE'):
            for tag in pmessage['configurationItemDiff']['changedProperties']['Configuration']['previousValue']['tags']:
                if tag['key'] == 'ApplicationID':
                    client = boto3.client('sqs')
                    response = client.send_message(
                        QueueUrl = os.environ['QUEUE_URL'],
                        MessageAttributes={
                            'type': {
                                'DataType': 'String',
                                'StringValue': 'awsconfig_cmdb'
                            },
                            'published_by': {
                                'DataType': 'String',
                                'StringValue': 'lambda' # Make Dynamic
                            },
                            'source': {
                                'DataType': 'String',
                                'StringValue': 'aws'
                            },
                            'transaction_id': {
                                'DataType': 'String',
                                'StringValue': pmessage['configurationItem']['configurationStateId']
                            },
                            'origin': {
                                'DataType': 'String',
                                'StringValue': 'aws'
                            },
                            'changeType': {
                                'DataType': 'String',
                                'StringValue': pmessage['configurationItemDiff']['changeType']
                            },
                            'create_time': {
                                'DataType': 'String',
                                'StringValue': pmessage['notificationCreationTime']
                            },
                            'awsAccountId': {
                                'DataType': 'String',
                                'StringValue': pmessage['configurationItem']['awsAccountId']
                            }
                        },
                        MessageBody=json.dumps(pmessage)
                    )
                    return response

    except KeyError:
        pass
