from smart_open import open
import boto3

from cog_ingester.config import aws_access_key_id, aws_secret_access_key


session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)


def copy_to_s3(local_path, remote_path, session=session):
  """
  Copy local file to remote S3 location
  """
  with open (
    remote_path,
    'wb',
    transport_params=dict(session=session)
  ) as sink:
    with open(local_path, 'rb') as source:
      sink.write(source.read())


def file_exists(path, session=session):
  """
  Check if file exists at path
  """
  try:
    with open(path, transport_params=dict(session=session)):
        file_exists = True
  except OSError:
    file_exists = False

  return file_exists


if __name__ == '__main__':
    pass
