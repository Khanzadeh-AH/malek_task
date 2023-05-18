FROM python:3.9.16-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN cat /etc/resolv.conf
RUN ip a
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY webapp/ .

CMD [ "python", "./app.py" ]