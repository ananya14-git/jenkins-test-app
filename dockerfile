dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY app.py test_app.py ./

RUN chmod +x app.py test_app.py

CMD ["python3", "app.py"]
