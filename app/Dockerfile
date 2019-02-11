FROM python:3.6

# opens up port 5000, Flask uses this by default
EXPOSE 5000

#create the workign directory
WORKDIR /rexchangeApplication

# use the requirements file, and install Flask / mysql
COPY requirements.txt /rexchangeApplication
RUN pip install -r requirements.txt

# Copy the application
COPY main.py /rexchangeApplication
# Run the application when the container starts.
CMD python main.py
