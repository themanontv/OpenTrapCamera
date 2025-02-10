import os
from modules import capture, aws, config

# Capture the scene
cwd = os.getcwd()
file = capture.photo(cwd)

# Get the config
aws_access_key, aws_secret_key, bucket = config.ingest(cwd + "/config")

# Upload file
session = aws.create_session(aws_access_key, aws_secret_key)
aws.upload(session, file, bucket)
