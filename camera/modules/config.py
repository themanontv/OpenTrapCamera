import sys
import configparser as conf


def ingest(file):
    """
    Ingests a config file at the top level of the repo
    """
    config = conf.ConfigParser()

    try:
        config.read(file)
    except FileNotFoundError:
        print("Failed to retrieve config file at " + file)
        sys.exit()

    # Get AWS information
    try:
        aws_access_key = config.get("AWS", "access_key")
        aws_secret_key = config.get("AWS", "secret_key")
        bucket_name = config.get("AWS", "bucket_name")
    except AttributeError:
        print("No AWS credentials specified in " + file)

    return aws_access_key, aws_secret_key, bucket_name
