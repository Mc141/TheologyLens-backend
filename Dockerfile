# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Download data at build time (or do it in CMD if you prefer runtime)
RUN python download_data.py

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "api.routes.main:app", "--host", "0.0.0.0", "--port", "8000"]
