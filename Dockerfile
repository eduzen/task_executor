FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:$PYTHONPATH
RUN mkdir /code
WORKDIR /code
COPY dev_requirements.txt requirements.txt /code/
RUN pip install -r dev_requirements.txt
COPY . /code/
