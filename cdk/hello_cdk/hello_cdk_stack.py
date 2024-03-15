import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_sns as sns
import aws_cdk.aws_sqs as sqs
import aws_cdk.aws_sns_subscriptions as subs

            
class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Bucket
        bucket = s3.Bucket(self, "MyFirstBucket",
          versioned=True,
          removal_policy=cdk.RemovalPolicy.DESTROY,
          auto_delete_objects=True)

        # Create an SNS topic
        topic = sns.Topic(self, "MyTopic")        

        # Create an SQS queue
        queue = sqs.Queue(self, "MyQueue")

        # Subscribe the SQS queue to the SNS topic
        topic.add_subscription(subs.SqsSubscription(queue))        

        # Grant permissions for SNS to send messages to the SQS queue
        #queue.grant_receive_messages(topic)