
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["streamlit", "run", "dashboards/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
