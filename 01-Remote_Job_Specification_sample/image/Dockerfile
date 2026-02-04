FROM python:3.7.17-slim

RUN  mkdir -m 775 -p /home/templates && \
  python3 -m pip install Jinja2 flask

ADD tplserver.py /home
ADD demo.yaml /home/templates
WORKDIR /home

ENV PYTHONPYCACHEPREFIX=/tmp
ENTRYPOINT ["python3", "/home/tplserver.py"]

EXPOSE 8080
