# Use official Python image as base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port (same as in Render)
EXPOSE 10000

# Command to run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
