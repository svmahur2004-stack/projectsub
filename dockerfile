FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run pytest
RUN pytest test_vote.py

# Run the application
CMD ["python", "vote.py"]