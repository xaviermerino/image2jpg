# Use the specified Python image from the dockerhub
FROM python:3.12-slim
LABEL org.opencontainers.image.source=https://github.com/xaviermerino/image2jpg
LABEL org.opencontainers.image.description="Convert HEIC, PNG, and TIFF to JPG"
# Set the working directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["python", "./convert_images.py"]
