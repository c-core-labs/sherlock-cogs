# coding: utf-8

from typing import Optional

from fastapi import FastAPI, HTTPException, Header
from starlette.middleware.cors import CORSMiddleware

import logging
from pystac import Item
from cog_ingester.main import main
from cog_ingester.schema import ProcessItemRequest, STACTranslateRequest, \
    SherlockTranslationRequest
from cog_ingester.stac import get_sherlock_stac, generate_cog


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
# sentry_sdk.init(dsn=sentry_dsn)


api = FastAPI(
    title="Cloud Optimized GeoTIFF Ingester",
    description="Create Cloud Optimized GeoTIFF on the cloud ☁",
)
api.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)



@api.get("/")
def health_check():
    """
    Health check

    The health check enpoint is used by container orchestrators to confirm the
    service is healthy.
    """
    status = { "status": "ok" }

    return status


@api.post("/cog/")
def process_cog(body: ProcessItemRequest):
    """
    Convert image at path to a Cloud Optimized GeoTIFF
    """
    try:
        result = main(body.source_path, body.destination_path)
    except Exception as exception:
        log.exception(exception)

        raise HTTPException(status_code=400, detail=f"{exception}")

    return result


@api.post("/stac/")
def process_stac_item(body: STACTranslateRequest):
    try:
        stac_item = Item.from_dict(body.item)

        return generate_cog(stac_item, body.destination_uri, body.target_assets)

    except Exception as exception:
        log.exception(exception)
        raise HTTPException(status_code=400, detail=f"{exception}")


@api.post("/sherlock/")
def process_sherlock_id(body: SherlockTranslationRequest, authorization: Optional[str]=Header(None)):
    try:
        stac_item = get_sherlock_stac(body.sherlock_id, authorization)
        return generate_cog(stac_item, body.destination_uri, body.target_assets)
    except Exception as exception:
        log.exception(exception)
        raise HTTPException(status_code=400, detail=f"{exception}")

if __name__ == "__main__":
    # Entry point for development
    # Production containers call `uvicorn` from bash shell (see Dockerfile)
    import uvicorn

    uvicorn.run(
        "cog_ingester.api:api",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        reload=True,
    )
