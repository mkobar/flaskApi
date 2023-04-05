# Dockerfile
# how to use: docker build -t isearch/flask-api:2.0.9 .

#FROM python:3.10-alpine
#FROM python:3.11.0b3-alpine3.16 - error in greenlet build
FROM python:3.11.3-alpine3.16
LABEL maintainer="Mike <mike@iterativesearch.com>"

# required for image build
RUN apk add make gcc g++ musl-dev -U
#RUN apk add make g++ musl-dev -U still adds gcc so no savings

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV API_KEY dummy
# below needed for pytest and docker-test
#export PYTHONPATH="${PATH}:/app"
ENV PYTHONPATH /usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/app

# Specify port
EXPOSE 5000

# start with "docker run -d -p 80:5000 --env API_KEY=api --name fapi isearch/flask-api:2.0.9"
CMD gunicorn -b 0.0.0.0:5000 --access-logfile - 'searchApi.app:create_app("config.settings_production")'
