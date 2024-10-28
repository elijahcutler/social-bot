# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Docker client inside the container
RUN apt-get update && apt-get install -y docker.io

# Run the bot when the container launches
CMD ["python", "bot.py"]