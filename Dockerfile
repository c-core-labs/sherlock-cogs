FROM python:3.8.5-buster as builder

# Install the C compiler tools
RUN apt-get update
RUN apt-get install -y build-essential cmake wget git pkg-config
RUN pip install --upgrade pip

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM python:3.8.5-slim as base
COPY --from=builder /install /usr/local
COPY cog_ingester /cog_ingester
# COPY google.json /google.json
# COPY cloud_storage.json /cloud_storage.json

CMD ["uvicorn", "cog_ingester.api:api", "--host", "0.0.0.0", "--port", "8080"]
