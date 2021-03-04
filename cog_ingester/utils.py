import requests
from config import LOGIN_URL, DEFAULT_BUCKET


def get_s3_path(uri, bucket=DEFAULT_BUCKET):
    """
    Get key from uri
    """
    client = uri.split('/')[3]
    project = uri.split('/')[4]
    name = uri.split('/', 5)[5]
    name = name.replace('/', '-')
    name = name.replace('ingest', '')
    name = name.replace('_', '-')
    name = name.replace(' ', '-')
    name = name.replace('---', '-')
    name = name.replace('--', '-')
    name = name.lower()
    id_ = name.split('-', 1)[1]

    path = f's3://{bucket}/{client}/{project}/{id_}'


    return path


def request_auth(username, password):
    """
    Retrieve auth token
    """

    resp = requests.post(url=LOGIN_URL,  body={username: username,  password: password})
    return resp.json()


if __name__ == '__main__':
    pass
