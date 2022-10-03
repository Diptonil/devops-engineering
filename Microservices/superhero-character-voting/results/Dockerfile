# Base the custom image created by us off python:3.9 image. 
FROM python:3.9

# Environment variable that lets us see console output of the Django app.
ENV PYTHONUNBUFFERED 1

# Sets up the working directory in the Docker environment.
WORKDIR /app/

# Copies requirements into the workspace requirements.
COPY requirements.txt /app/requirements.txt

# Run command to install dependencies
RUN pip install -r requirements.txt

COPY . /app/

# Expose port 800 to the traffic.
EXPOSE 8000

# Execue given command.
CMD python manage.py runserver 0.0.0.0

