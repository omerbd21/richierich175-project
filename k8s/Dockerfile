FROM python:3.9

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r ../python/requirements.txt

EXPOSE 8080
CMD ["python", "/app/main.py"]
