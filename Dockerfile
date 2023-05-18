FROM python:3.9.16-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY webapp/ .

CMD [ "python", "./app.py" ]