# Use a base image that has the necessary dependencies for you script
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the AI code in the container
COPY AIProject.py .

# Install any required dependencies
RUN pip isntall numpy tensorflow

# Set the command to run your AI code
CMD ["python", "AIProject.py"]