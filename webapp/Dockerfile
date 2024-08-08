FROM python:3.9-slim

WORKDIR /app

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt /app/requirements.txt

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80

CMD ["python", "app.py"]
