# Using avalanche base image
FROM avalanche-claas:base-skeleton-v1 

# Set the application directory
WORKDIR /claas
# Copy our code from the current folder to /claas inside the container
COPY . .

# Install CLaas dep using pip in conda
RUN echo "conda activate avalanche-env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]
RUN pip install -r requirements.txt


# Make port 5000 available for links and/or publish
EXPOSE 5000

#TODO: here!