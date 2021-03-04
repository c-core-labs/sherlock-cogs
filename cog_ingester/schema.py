from typing import Optional, List, Dict
from pydantic import BaseModel


class ProcessItemRequest(BaseModel):
    source_path: str
    destination_path: Optional[str] = None
    force: bool = False

    class Config:
        schema_extra = {
            "example": {
                "source_path": "s3://sentinel-s2-l1c/tiles/10/S/DG/2015/12/7/0/B03.jp2",
                "destination_path": "s3://c-core-public/cog-sample.tif",
                "force": False,
            }
        }


class STACTranslateRequest(BaseModel):
    item: Dict
    target_assets:  List[int]
    destination_uri: str

    class Config:
        schema_extra = {
            "example": {
                "item":         {
            "type": "Feature",
            "geometry": {
                "coordinates": [
                    [
                        [
                            -78.77222464368829,
                            41.43811567133993
                        ],
                        [
                            -76.53338601561056,
                            40.96307533377448
                        ],
                        [
                            -77.17632663689072,
                            39.20469789738642
                        ],
                        [
                            -79.41309882196701,
                            39.686096346456495
                        ],
                        [
                            -78.77222464368829,
                            41.43811567133993
                        ]
                    ]
                ],
                "type": "Polygon"
            },
            "properties": {
                "created": "2020-11-16T20:00:53Z",
                "updated": "2020-12-02T16:23:33Z",
                "platform": "LANDSAT_8",
                "instruments": [
                    "OLI",
                    "TIRS"
                ],
                "gsd": 30.0,
                "datetime": "2020-11-09T15:52:31Z",
                "landsat:scene_id": "LC80160322020314LGN00",
                "view:sun_azimuth": 162.3979503,
                "proj:epsg": 32618,
                "landsat:cloud_cover_land": -1,
                "landsat:wrs_path": "16",
                "view:sun_elevation": 30.7066987,
                "eo:cloud_cover": -1,
                "landsat:wrs_row": "32",
                "landsat:collection_category": "T1",
                "landsat:collection_number": "01",
                "view:off_nadir": 0.001,
                "landsat:processing_level": "L1TP"
            },
            "id": "LC08_L1TP_016032_20201109_20201112_01_T1",
            "bbox": [
                -79.41389,
                39.20193,
                -76.53252,
                41.4399
            ],
            "stac_version": "1.0.0-beta.2",
            "assets": {
                "B1": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B1.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B1",
                            "common_name": "coastal",
                            "center_wavelength": 0.48,
                            "full_width_half_max": 0.02
                        }
                    ]
                },
                "B2": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B2.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B2",
                            "common_name": "blue",
                            "center_wavelength": 0.44,
                            "full_width_half_max": 0.06
                        }
                    ]
                },
                "B3": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B3.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B3",
                            "common_name": "green",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.06
                        }
                    ]
                },
                "B4": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B4.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B4",
                            "common_name": "red",
                            "center_wavelength": 0.65,
                            "full_width_half_max": 0.04
                        }
                    ]
                },
                "B5": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B5.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B5",
                            "common_name": "nir",
                            "center_wavelength": 0.86,
                            "full_width_half_max": 0.03
                        }
                    ]
                },
                "B6": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B6.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B6",
                            "common_name": "swir16",
                            "center_wavelength": 1.6,
                            "full_width_half_max": 0.08
                        }
                    ]
                },
                "B7": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B7.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B7",
                            "common_name": "swir22",
                            "center_wavelength": 2.2,
                            "full_width_half_max": 0.2
                        }
                    ]
                },
                "B8": {
                    "gsd": 15.0,
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B8.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B8",
                            "common_name": "pan",
                            "center_wavelength": 0.59,
                            "full_width_half_max": 0.18
                        }
                    ]
                },
                "B9": {
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B9.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B9",
                            "common_name": "cirrus",
                            "center_wavelength": 1.37,
                            "full_width_half_max": 0.02
                        }
                    ]
                },
                "ANG": {
                    "title": "ANG Metadata",
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_ANG.txt",
                    "type": "text/plain",
                    "roles": [
                        "metadata"
                    ]
                },
                "B10": {
                    "gsd": 100.0,
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B10.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B10",
                            "common_name": "lwir11",
                            "center_wavelength": 10.9,
                            "full_width_half_max": 0.8
                        }
                    ]
                },
                "B11": {
                    "gsd": 100.0,
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_B11.TIF",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "eo:bands": [
                        {
                            "name": "B11",
                            "common_name": "lwir12",
                            "center_wavelength": 12.0,
                            "full_width_half_max": 1.0
                        }
                    ]
                },
                "BQA": {
                    "title": "Quality Band",
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_BQA.TIF",
                    "type": "image/tiff; application=geotiff",
                    "roles": [
                        "metadata"
                    ]
                },
                "MTL": {
                    "title": "MTL Metadata",
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_MTL.txt",
                    "type": "text/plain",
                    "roles": [
                        "metadata"
                    ]
                },
                "index": {
                    "title": "HTML Page",
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/index.html",
                    "type": "application/html"
                },
                "thumbnail": {
                    "title": "Thumbnail",
                    "href": "https://landsat-pds.s3.us-west-2.amazonaws.com/c1/L8/016/032/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1_thumb_large.jpg",
                    "type": "image/jpeg",
                    "roles": [
                        "thumbnail"
                    ]
                }
            },
            "links": [
                {
                    "href": "http://stac-api.c-core.app/collections/landsat-8-l1-c1/items/LC08_L1TP_016032_20201109_20201112_01_T1",
                    "rel": "self",
                    "type": "application/geo+json"
                },
                {
                    "href": "http://stac-api.c-core.app/collections/landsat-8-l1-c1",
                    "rel": "parent",
                    "type": "application/json"
                },
                {
                    "href": "http://stac-api.c-core.app/collections/landsat-8-l1-c1",
                    "rel": "collection",
                    "type": "application/json"
                },
                {
                    "href": "http://stac-api.c-core.app/",
                    "rel": "root",
                    "type": "application/json"
                },
                {
                    "href": "http://stac-api.c-core.app/collections/landsat-8-l1-c1/items/LC08_L1TP_016032_20201109_20201112_01_T1/tiles",
                    "rel": "alternate",
                    "type": "application/json",
                    "title": "tiles"
                },
                {
                    "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/landsat-8-l1-c1/16/32/2020/11/LC08_L1TP_016032_20201109_20201112_01_T1/LC08_L1TP_016032_20201109_20201112_01_T1.json",
                    "rel": "canonical",
                    "type": "application/json"
                },
                {
                    "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/landsat-8-l1-c1-aws/workflow-publish-landsat/LC08_L1TP_016032_20201109_20201112_01_T1",
                    "rel": "via-cirrus",
                    "title": "landsat-8-l1-c1-aws/workflow-publish-landsat/LC08_L1TP_016032_20201109_20201112_01_T1"
                }
            ],
            "stac_extensions": [
                "eo",
                "projection",
                "view",
                "landsat"
            ],
            "collection": "landsat-8-l1-c1"
        },
                "target_assets": ['B11', 'B04', 'B03'],
                "destination_uri": "s3://TARGET_BUCKET/landsat8",
                "force": True,
            }
        }


class SherlockTranslationRequest(BaseModel):
    sherlock_id: str
    target_assets: List[str]
    destination_uri: str

    class Config:
        schema_extra = {
            "example": {"sherlock_id": "LC08_L1TP_016032_20201109_20201112_01_T1",
                        "target_assets": ['B11', 'B04', 'B03'],
                        "destination_uri": "s3://TARGET_BUCKET/landsat8",
                        }
        }

if __name__ == '__main__':
    pass
