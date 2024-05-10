FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install Flask sqlalchemy psycopg2-binary

EXPOSE 5000

CMD ["python", "app.py"]
