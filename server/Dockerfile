# Specify lightweight docker image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy  and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy code and files
COPY . .

# Expose port
EXPOSE 5000
# Execute
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
