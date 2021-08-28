FROM python:3.9.6-alpine3.14
WORKDIR /app
ADD . /app
RUN pip install flask
RUN pip install flask-cors
EXPOSE 80
EXECUTE ["python", "main.py"]
