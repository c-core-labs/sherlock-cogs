import os
from dotenv import load_dotenv


# Fix for fiona/gdal not finding ssl certificates:
# https://github.com/cogeotiff/rio-tiler/issues/53#issuecomment-412198813
os.environ["CURL_CA_BUNDLE"] = "/etc/ssl/certs/ca-certificates.crt"

# Load .env file into environment variables
load_dotenv()

aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")

sengrid_api_key = os.environ.get("SENDGRID_API_KEY")

sentry_dsn = os.environ.get("SENTRY_DSN")

LOGIN_URL = os.environ.get('LOGIN_URL')
STAC_API = os.environ.get('SHERLOCK_API_URL')
STAC_USERNAME = os.environ.get('USERNAME')
STAC_PASSWORD = os.environ.get('PASSWORD')
DEFAULT_BUCKET = os.environ.get('DEFAULT_BUCKET')

if __name__ == '__main__':
    pass
