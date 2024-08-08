FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Run the script to create the executable and upload to S3
RUN chmod +x create_exe.sh && ./create_exe.sh

CMD ["python", "game.py"]
