# get lighter version (3.7-alphine) from python official image
FROM python:3.7-alpine 

# to not have python buffer (recommended for basic python)
ENV PYTHONUNBUFFERED 1

# copy from local requirements.txt to docker requirements.txt
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

# creates app folder and switch into that folder
RUN mkdir /app
WORKDIR /app

# copy our ./app to /app in the docker
COPY ./app /app

# add "user" to user and change to "user"
# if you don't do this, image uses root account, 
# this is not recommended for security purposes
RUN adduser -D user
USER user




