FROM python:3.11-slim

WORKDIR /app

COPY requierments.txt .

RUN pip install -r requierments.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]

