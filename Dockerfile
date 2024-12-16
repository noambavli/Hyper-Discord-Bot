FROM python:3.10-slim

# Set the working directory
WORKDIR ./

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy bot code
COPY . .

# Run the bot
CMD ["python3", "main.py"]
