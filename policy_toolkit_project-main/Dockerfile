# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for geopandas (GDAL, GEOS, PROJ)
RUN apt-get update && apt-get install -y     build-essential     gdal-bin     libgdal-dev     libgeos-dev     libproj-dev     && rm -rf /var/lib/apt/lists/*

# Copy project files into container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Streamlit runs in headless mode inside Docker
CMD ["streamlit", "run", "dashboards/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
