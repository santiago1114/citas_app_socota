# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Install git for install dependencies from pip
RUN apk update && apk upgrade

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements to the container (WORKDIR) and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the container app folder
COPY ./src .

# Copy and execute entrypoint
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
