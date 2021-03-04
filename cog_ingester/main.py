from tempfile import NamedTemporaryFile
import logging

from cog_ingester.cog import create_cog
from cog_ingester.utils import get_s3_path
from cog_ingester.storage import copy_to_s3
from cog_ingester.timer import timer


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@timer
def main(source_uri, destination_uri = None):
    """
    Create COG and copy to cloud storage
    """
    if not destination_uri:
        # Try to guess destination uri
        destination_uri = get_s3_path(source_uri)

    with NamedTemporaryFile() as file:
        log.info(f'Create cloud optimized geotiff from {source_uri}')
        local_uri = create_cog(source_uri, file.name)
        log.info(f'Copying {local_uri} to  {destination_uri}')
        copy_to_s3(local_uri, destination_uri)

    return {
        'destination_uri': destination_uri
    }


if __name__ == '__main__':
    pass
