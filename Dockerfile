FROM python:3.9-slim-buster

WORKDIR /app

COPY app.py .
COPY static/script.js static/
COPY static/style.css static/
COPY templates/index.html templates/
#COPY ./ ./

RUN pip install flask

EXPOSE 7019

CMD ["python", "app.py"]