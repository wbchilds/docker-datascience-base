FROM jupyter/datascience-notebook as base

COPY requirements.txt /

RUN pip install -r /requirements.txt

 
