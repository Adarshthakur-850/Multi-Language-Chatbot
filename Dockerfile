FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install NLTK/Spacy data if needed (not needed for this specific stack but good practice)

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
