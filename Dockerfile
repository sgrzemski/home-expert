FROM python:3.10

WORKDIR /app

COPY src/ /app

RUN pip3 install -r /app/requirements.txt

EXPOSE 8080
ENTRYPOINT ["python3", "/app/main.py"]
