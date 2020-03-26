import boto3


def create_s3_client(bucket):
    pass


def create_s3_resource(region_name):
    """
    Create an S3 Resource.
    """
    return boto3.resource('s3', region_name=region_name)
