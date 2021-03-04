# COG Ingester

Create Cloud Optimized GeoTIFF on the cloud ☁

## Get Started

This container is for the creation of a service to web optimized images from input 
raster imagery. The intended use of this container is to create streamable cogs from 
geo-referenced imagery in cloud storage on AWS for use in analysis pipelines  

## How to build container

## Environment variables
In order to execute you will have to create an .env file from the .env.example file that 
provides your implementation details. The required environment variables are    

- `AWS_ACCESS_KEY_ID` - Access Key for AWS user with permission to access s3 resources.
- `AWS_SECRET_ACCESS_KEY` - Secret Access Key for AWS user with permission to access s3 resources.
- `SHERLOCK_API_URL` - URL of sherlock instance.
- `LOGIN_URL` - Sherlock Oauth2 token source login.
- `USER_NAME` - Sherlock Username.
- `PASSWORD` - Sherlock Password.
- `DEFAULT_BUCKET` - default location to store outputs.

If you have a environment variable file e S3 bucket for convenience.

``` shell
aws s3 cp s3://c-core-secure/config/cog-ingester/.env .env
```



##Development

### Install Poetry
https://python-poetry.org/docs/#installation

``` shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Install dependencies

``` shell
poetry install
```

### Run Develop Server 

``` shell
poetry run start
```

### Docker

``` shell
poetry run docker
```

### Deploy

``` shell
poetry run deploy
```

## How to Run Container

1. Install Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Update environmental variables   
3. From the project root build Docker file using `docker build .--tag sherlock-cog:latest`
4. to run locally use `docker start sherlock-cog:latest`
5. alternatively, you can deploy to a repository using the docker push and pull
   commands to deploy to a server.
   
## Supported Datasets

The Sherlock Cog ingestion container should be able to work on datasets that cloud 
hosted raster imagery that need to be converted to web-optimized STAC format.

## How to use

Once the container is up and running, you can connect to the api through the `/stac/` and `/sherlock/` endpoints. Api documentation us avakabke at `/docs`

`stac`:
parameters:
`stac_item`: json representation of stac item
`targetted_assets`: list of assets to convert to cog
`destination_uri`: s3 uri for destination

`sherlock`:
parameters:
`sherlock_id`: id of item from sherlock
`targetted_assets`: list of assets to convert to cog
`destination_uri`: s3 uri for destination




## link to sherlock
