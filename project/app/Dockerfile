FROM --platform=linux/arm64/v8 python:3.12.3 as build

#  Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
#  Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
# Fixed problem with pip installing without root permissions
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /src/app

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .