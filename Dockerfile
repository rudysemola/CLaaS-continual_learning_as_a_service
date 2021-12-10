# Using official python runtime base image
FROM continuumio/miniconda3

# Set the application directory
WORKDIR /claas
# Copy our code from the current folder to /claas inside the container
COPY . .

#Setup avalanche in claas (local - CPU only!)
RUN bash install_environment.sh 
WORKDIR /claas

# Make port 5000 available for links and/or publish
EXPOSE 5000

# Define our command to be run when launching the container
CMD ["/bin/bash", "run.sh"]
