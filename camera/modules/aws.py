import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def create_session(access_key, secret_key):
    """
    Creates a boto3 session
    """
    session = boto3.Session(aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key
                            )
    return session


def upload(session, file_path, bucket_name, s3_file_name=None):
    """
    Uploads a file to an S3 bucket.
    :param file_path: The local path to the file to upload.
    :param bucket_name: The name of the S3 bucket.
    :param s3_file_name: The name of the file in S3 (optional).
    :return: True if file was uploaded, else False.
    """
    # If no S3 file name is provided, use the local file name
    if s3_file_name is None:
        s3_file_name = file_path.split('/')[-1]

    # Create an S3 client
    s3_client = session.client('s3')

    try:
        # Upload the file
        s3_client.upload_file(file_path, bucket_name, s3_file_name)
        print(f"File {file_path} uploaded to {bucket_name}/{s3_file_name}.")
        return True
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
