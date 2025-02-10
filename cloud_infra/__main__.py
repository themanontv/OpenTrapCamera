"""AWS Infrastructure for the OpenTrapCamera Project"""

import pulumi
from pulumi_aws import s3
from pulumi_aws import iam

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2('image-bucket')
# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)