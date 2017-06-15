FROM python:3.6.1-alpine3.6
ARG APP=${APP:-/srv/app}
RUN mkdir -p $APP
WORKDIR $APP
ADD qrcode-generator $APP
RUN apk add --no-cache build-base python3-dev jpeg-dev zlib-dev && \
	pip install --no-cache-dir -r requirements.txt && \
	apk del build-base python3-dev jpeg-dev zlib-dev && \
	apk add --no-cache libjpeg-turbo
EXPOSE 5000
CMD [ "python", "main.py" ]
