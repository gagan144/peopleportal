FROM python:3.6-slim

# Install linux dependencies
RUN apt update
RUN python -m pip install --upgrade pip
RUN apt -y install gcc libpq-dev python3-dev


# Set working directory
WORKDIR /app


# Install Python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip cache purge


# Setup Application
COPY . .
COPY ./peopleportal/_settings_docker.py ./peopleportal/settings.py


# Setup uwsgi
RUN pip install uwsgi==2.0.19.1


# Setup entry point to run uwsgi server via shell script
RUN chmod 776 docker-entrypoint.sh
CMD bash -C '/app/docker-entrypoint.sh';'bash'