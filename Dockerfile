# Use the official Python image as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Specify the command to run your application
CMD ["python", "app.py"]
