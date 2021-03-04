import subprocess
from rio_cogeo.cogeo import cog_translate
from rio_cogeo import version as cogeo_version
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def create_cog(uri, destination = 'out.tif'):
  """
  Create COG from uri
  """
  log.info(f'Creating COG from {uri}')
  result = subprocess.run([
      'rio',
      'cogeo',
      'create',
      uri,
      destination,
      '--web-optimized',
  ],
  stderr=subprocess.DEVNULL)

  return destination


if __name__ == '__main__':
    pass
