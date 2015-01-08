import datetime
from dateutil.tz import tzutc

cfn_list_stack_resources = [{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'dd35f0ef-9699-11e4-ba38-c355c9515dbc'}, u'StackResourceSummaries': [{u'ResourceStatus': 'CREATE_COMPLETE', u'ResourceType': 'AWS::IAM::Role', u'ResourceStatusReason': None, u'LastUpdatedTimestamp': datetime.datetime(2015, 1, 6, 17, 37, 54, 861000, tzinfo=tzutc()), u'PhysicalResourceId': 'TestKinesis-InvokeRole-IF6VUXY9MBJN', u'LogicalResourceId': 'InvokeRole'}, {u'ResourceStatus': 'CREATE_COMPLETE', u'ResourceType': 'AWS::IAM::Role', u'ResourceStatusReason': None, u'LastUpdatedTimestamp': datetime.datetime(2015, 1, 6, 17, 37, 55, 18000, tzinfo=tzutc()), u'PhysicalResourceId': 'TestKinesis-ExecRole-567SAV6TZOET', u'LogicalResourceId': 'ExecRole'}, {u'ResourceStatus': 'CREATE_COMPLETE', u'ResourceType': 'AWS::IAM::Policy', u'ResourceStatusReason': None, u'LastUpdatedTimestamp': datetime.datetime(2015, 1, 6, 17, 37, 58, 120000, tzinfo=tzutc()), u'PhysicalResourceId': 'TestK-Invo-OMW5SDLQM8FM', u'LogicalResourceId': 'InvokeRolePolicies'}, {u'ResourceStatus': 'CREATE_COMPLETE', u'ResourceType': 'AWS::IAM::Policy', u'ResourceStatusReason': None, u'LastUpdatedTimestamp': datetime.datetime(2015, 1, 6, 17, 37, 58, 454000, tzinfo=tzutc()), u'PhysicalResourceId': 'TestK-Exec-APWRVKTBPPPT', u'LogicalResourceId': 'ExecRolePolicies'}]}]

iam_get_role = [{u'Role': {u'AssumeRolePolicyDocument': {u'Version': u'2012-10-17', u'Statement': [{u'Action': u'sts:AssumeRole', u'Principal': {u'Service': u's3.amazonaws.com'}, u'Effect': u'Allow', u'Condition': {u'ArnLike': {u'sts:ExternalId': u'arn:aws:s3:::*'}}, u'Sid': u''}, {u'Action': u'sts:AssumeRole', u'Principal': {u'Service': u'lambda.amazonaws.com'}, u'Effect': u'Allow', u'Sid': u''}]}, u'RoleId': 'AROAIEVJHUJG2I4MG5PSC', u'CreateDate': datetime.datetime(2015, 1, 6, 17, 37, 44, tzinfo=tzutc()), u'RoleName': 'TestKinesis-InvokeRole-IF6VUXY9MBJN', u'Path': '/', u'Arn': 'arn:aws:iam::0123456789012:role/TestKinesis-InvokeRole-FOO'}, 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'dd6e8d42-9699-11e4-afe6-d3625e8b365b'}}]

logs_describe_log_streams = [{u'logStreams': [{u'firstEventTimestamp': 1417042749449, u'lastEventTimestamp': 1417042749547, u'creationTime': 1417042748263, u'uploadSequenceToken': u'49540114640150833041490484409222729829873988799393975922', u'logStreamName': u'1cc48e4e613246b7974094323259d600', u'lastIngestionTime': 1417042750483, u'arn': u'arn:aws:logs:us-east-1:0123456789012:log-group:/aws/lambda/KinesisSample:log-stream:1cc48e4e613246b7974094323259d600', u'storedBytes': 712}, {u'firstEventTimestamp': 1417272406988, u'lastEventTimestamp': 1417272407088, u'creationTime': 1417272405690, u'uploadSequenceToken': u'49540113907504451034164105858363493278561872472363261986', u'logStreamName': u'2782a5ff88824c85a9639480d1ed7bbe', u'lastIngestionTime': 1417272408043, u'arn': u'arn:aws:logs:us-east-1:0123456789012:log-group:/aws/lambda/KinesisSample:log-stream:2782a5ff88824c85a9639480d1ed7bbe', u'storedBytes': 712}, {u'firstEventTimestamp': 1420569035842, u'lastEventTimestamp': 1420569035941, u'creationTime': 1420569034614, u'uploadSequenceToken': u'49540113907883563702539166025438885323514410026454245426', u'logStreamName': u'2d62991a479b4ebf9486176122b72a55', u'lastIngestionTime': 1420569036909, u'arn': u'arn:aws:logs:us-east-1:0123456789012:log-group:/aws/lambda/KinesisSample:log-stream:2d62991a479b4ebf9486176122b72a55', u'storedBytes': 709}, {u'firstEventTimestamp': 1418244027421, u'lastEventTimestamp': 1418244027541, u'creationTime': 1418244026907, u'uploadSequenceToken': u'49540113964795065449189116778452984186276757901477438642', u'logStreamName': u'4f44ffa128d6405591ca83b2b0f9dd2d', u'lastIngestionTime': 1418244028484, u'arn': u'arn:aws:logs:us-east-1:0123456789012:log-group:/aws/lambda/KinesisSample:log-stream:4f44ffa128d6405591ca83b2b0f9dd2d', u'storedBytes': 1010}, {u'firstEventTimestamp': 1418242565524, u'lastEventTimestamp': 1418242565641, u'creationTime': 1418242564196, u'uploadSequenceToken': u'49540113095132904942090446312687285178819573422397343074', u'logStreamName': u'69c5ac87e7e6415985116e8cb44e538e', u'lastIngestionTime': 1418242566558, u'arn': u'arn:aws:logs:us-east-1:0123456789012:log-group:/aws/lambda/KinesisSample:log-stream:69c5ac87e7e6415985116e8cb44e538e', u'storedBytes': 713}, {u'firstEventTimestamp': 1417213193378, u'lastEventTimestamp': 1417213193478, u'creationTime': 1417213192095, u'uploadSequenceToken': u'49540113336360065754596187770479764234792559857643841394', u'logStreamName': u'f68e3d87b8a14cdba338f6926f7cf50a', u'lastIngestionTime': 1417213194421, u'arn': u'arn:aws:logs:us-east-1:0123456789012:log-group:/aws/lambda/KinesisSample:log-stream:f68e3d87b8a14cdba338f6926f7cf50a', u'storedBytes': 711}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '2a6d4941-969b-11e4-947f-19d1c72ede7e'}}]

logs_get_log_events = [{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '2a7deb71-969b-11e4-914b-8f1f3d7b023d'}, u'nextForwardToken': u'f/31679748107442531967654742688057700554200447759088287749', u'events': [{u'ingestionTime': 1420569036909, u'timestamp': 1420569035842, u'message': u'2015-01-06T18:30:35.841Z\tko2sss03iq7l2pdk\tLoading event\n'}, {u'ingestionTime': 1420569036909, u'timestamp': 1420569035899, u'message': u'START RequestId: 23007242-95d2-11e4-a10e-7b2ab60a7770\n'}, {u'ingestionTime': 1420569036909, u'timestamp': 1420569035940, u'message': u'2015-01-06T18:30:35.940Z\t23007242-95d2-11e4-a10e-7b2ab60a7770\t{\n  "Records": [\n    {\n      "kinesis": {\n        "partitionKey": "partitionKey-3",\n        "kinesisSchemaVersion": "1.0",\n        "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0IDEyMy4=",\n        "sequenceNumber": "49545115243490985018280067714973144582180062593244200961"\n      },\n      "eventSource": "aws:kinesis",\n      "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",\n      "invokeIdentityArn": "arn:aws:iam::0123456789012:role/testLEBRole",\n      "eventVersion": "1.0",\n      "eventName": "aws:kinesis:record",\n      "eventSourceARN": "arn:aws:kinesis:us-east-1:35667example:stream/examplestream",\n      "awsRegion": "us-east-1"\n    }\n  ]\n}\n'}, {u'ingestionTime': 1420569036909, u'timestamp': 1420569035940, u'message': u'2015-01-06T18:30:35.940Z\t23007242-95d2-11e4-a10e-7b2ab60a7770\tDecoded payload: Hello, this is a test 123.\n'}, {u'ingestionTime': 1420569036909, u'timestamp': 1420569035941, u'message': u'END RequestId: 23007242-95d2-11e4-a10e-7b2ab60a7770\n'}, {u'ingestionTime': 1420569036909, u'timestamp': 1420569035941, u'message': u'REPORT RequestId: 23007242-95d2-11e4-a10e-7b2ab60a7770\tDuration: 98.51 ms\tBilled Duration: 100 ms \tMemory Size: 128 MB\tMax Memory Used: 26 MB\t\n'}], u'nextBackwardToken': u'b/31679748105234758193000210997045664445208259969996226560'}]

cfn_describe_stacks = [
    {u'Stacks': [{u'StackId': 'arn:aws:cloudformation:us-east-1:084307701560:stack/TestKinesis/7c4ae730-96b8-11e4-94cc-5001dc3ed8d2', u'Description': None, u'Tags': [], u'StackStatusReason': 'User Initiated', u'CreationTime': datetime.datetime(2015, 1, 7, 21, 59, 43, 208000, tzinfo=tzutc()), u'Capabilities': ['CAPABILITY_IAM'], u'StackName': 'TestKinesis', u'NotificationARNs': [], u'StackStatus': 'CREATE_IN_PROGRESS', u'DisableRollback': False}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '7d66debd-96b8-11e4-a647-4f4741ffff69'}},
    {u'Stacks': [{u'StackId': 'arn:aws:cloudformation:us-east-1:084307701560:stack/TestKinesis/7c4ae730-96b8-11e4-94cc-5001dc3ed8d2', u'Description': None, u'Tags': [], u'StackStatusReason': 'User Initiated', u'CreationTime': datetime.datetime(2015, 1, 7, 21, 59, 43, 208000, tzinfo=tzutc()), u'Capabilities': ['CAPABILITY_IAM'], u'StackName': 'TestKinesis', u'NotificationARNs': [], u'StackStatus': 'CREATE_IN_PROGRESS', u'DisableRollback': False}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '7e36fff7-96b8-11e4-af44-6350f4f8c2ae'}},
    {u'Stacks': [{u'StackId': 'arn:aws:cloudformation:us-east-1:084307701560:stack/TestKinesis/7c4ae730-96b8-11e4-94cc-5001dc3ed8d2', u'Description': None, u'Tags': [], u'StackStatusReason': 'User Initiated', u'CreationTime': datetime.datetime(2015, 1, 7, 21, 59, 43, 208000, tzinfo=tzutc()), u'Capabilities': ['CAPABILITY_IAM'], u'StackName': 'TestKinesis', u'NotificationARNs': [], u'StackStatus': 'CREATE_IN_PROGRESS', u'DisableRollback': False}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '7ef03e10-96b8-11e4-bc86-7f67e11abcfa'}},
    {u'Stacks': [{u'StackId': 'arn:aws:cloudformation:us-east-1:084307701560:stack/TestKinesis/7c4ae730-96b8-11e4-94cc-5001dc3ed8d2', u'Description': None, u'Tags': [], u'StackStatusReason': None, u'CreationTime': datetime.datetime(2015, 1, 7, 21, 59, 43, 208000, tzinfo=tzutc()), u'Capabilities': ['CAPABILITY_IAM'], u'StackName': 'TestKinesis', u'NotificationARNs': [], u'StackStatus': 'CREATE_COMPLETE', u'DisableRollback': False}], 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '8c2bff8e-96b8-11e4-be70-c5ad82c32f2d'}}]

cfn_create_stack = [{u'StackId': 'arn:aws:cloudformation:us-east-1:084307701560:stack/TestKinesis/7c4ae730-96b8-11e4-94cc-5001dc3ed8d2', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '7c2f2260-96b8-11e4-be70-c5ad82c32f2d'}}]

cfn_delete_stack = [{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'f19af5b8-96bc-11e4-860e-11ba752b58a9'}}]
