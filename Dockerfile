# Base image.
FROM python:3.6

#Configure base container directory 
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app

# run development server
CMD python manage.py run -h 0.0.0.0