
import logging
from os.path import join, basename
from typing import List

import requests
from fastapi import HTTPException
from pystac import Item, Asset, MediaType

from cog_ingester.config import STAC_USERNAME, STAC_PASSWORD, LOGIN_URL, STAC_API
from cog_ingester.main import main
from cog_ingester.utils import request_auth


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def get_sherlock_stac(stac_id, auth=None):
    if not auth:
        if STAC_USERNAME and STAC_PASSWORD and LOGIN_URL:
            token = request_auth(STAC_USERNAME, STAC_USERNAME)
            auth = 'Bearer {0}'.format(token.get('access_token'))

    req = requests.get(join(STAC_API, 'search?ids={0}'.format(stac_id)),
                       headers={'Authorization': auth})

    resp = req.json()
    features = resp.get('features')
    if features is None:
        raise HTTPException(400, 'Sherlock failed to retrieve results.')
    if len(features) == 0:
        raise HTTPException(400, 'Sherlock ID did not match any records.')
    elif len(features)> 1:
        raise HTTPException(500, 'Sherlock ID returned ambiguous results.')

    stac_item = features[0]
    if not 'stac_version' in stac_item:
        stac_item['stac_version'] = 'v1.0.0-beta.2]'

    return Item.from_dict(features[0])


def generate_cog(stac_item: Item, destination_uri: str, target_assets: List):
    """

    """
    for input_layer in target_assets:
        asset = stac_item.assets.get(input_layer)
        result = main(asset.href, join(destination_uri, basename(asset.href)))

        asset.add_asset("{}_cog".format(input_layer),
                        Asset(href=result['destination_layer'], title=asset.title,
                              description=asset.description,
                              media_type=MediaType.COG,
                              roles=asset.roles,
                              properties=asset.properties))
    return stac_item.to_dict()


if __name__ == '__main__':
    pass
