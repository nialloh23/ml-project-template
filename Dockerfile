# docker build -t rtrautomation/ds-scripts:tfrs_1.0 . --build-arg PIP_INDEX_URL='https://user:pwd@artifactory.rtr.cloud/artifactory/api/pypi/pypi/simple'
# docker run -it --rm -v $(pwd):/code/relevance_engine/ -v ~/.aws/credentials:/root/.aws/credentials -v /tmp/data_sci/secrets.ini:/etc/data_sci/secrets.ini relevance-engine bash

# 1. Specify base/parent image
FROM tensorflow/tensorflow:latest-gpu

# 2.  Create the working directories
RUN mkdir -p /code/tf_reccomend
WORKDIR /code/tf_reccomend

# 3. Copy requirements file into container and install all required packages
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
ARG PIP_INDEX_URL
RUN pip install -r requirements.txt --index-url="$PIP_INDEX_URL"

WORKDIR /code/tf_reccomend/tfrs

# 4. Copy all the code from project into the container -> ignores docker ignore exclusions
COPY . /code/tf_reccomend