# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (Google Cloud Run uses this port)
EXPOSE 8080

# Run Flask using Gunicorn (for production)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "flask_app:app"]
