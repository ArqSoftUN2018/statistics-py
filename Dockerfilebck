FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /statistics_service
WORKDIR /statistics_service
ADD requirements.txt /statistics_service/
RUN pip install -r requirements.txt
ADD . /statistics_service/
