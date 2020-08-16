FROM python:3.8.5

COPY . /local
WORKDIR /local

RUN pip install -r requirements.txt

CMD ./gdyndns.py