# Introduction 

The current webapp generate QR codes from strings.

# Getting Started

To run the image, simply run the following command:
```shell
docker-compose up -d
```

This will build the image if not already built and starts the docker container.

By default, you can access the generator at address: http://localhost:8000/api/v1/qrcode/<data>.

There is 2 another endpoints: `/ping` and `/health` which you can use to verify if the service is up and running.

# Build and Test

To build the image, simply run the following command:
```shell
docker-compose build
```

# Contribute

Feel free to contribute and modify sources...
