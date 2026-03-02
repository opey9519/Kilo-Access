FROM python:3.12-slim

WORKDIR /app

# Install psql client
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["./wait-for-db.sh", "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]