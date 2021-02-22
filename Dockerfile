FROM python:3.8

COPY requirements.txt /requirements.txt
COPY doris /doris
RUN pip install -r requirements.txt
WORKDIR /
ENV PORT=80
ENTRYPOINT ["python", "-m", "doris"]
