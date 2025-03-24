# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt from the current directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set environment variables


# Expose port 8080 (Google Cloud Run uses this port)
EXPOSE 8080

# Run Flask using Gunicorn (for production)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "run:app", "--log-level", "debug"]
