# Multi-Language Chatbot

A real-time chatbot capable of understanding and responding in multiple languages using NLP and FastAPI.

## Features
- **Multi-language Support**: Detects user language and translates responses back.
- **Intent Detection**: Uses TF-IDF and Logistic Regression.
- **Knowledge Retrieval**: Cosine similarity search over FAQ knowledge base.
- **Real-time Chat**: WebSocket-based communication.
- **Web Interface**: Clean HTML/CSS/JS frontend.

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server**
   ```bash
   python main.py
   ```

3. **Access the Chat**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Docker

Build and run with Docker:
```bash
docker build -t chatbot .
docker run -p 8000:8000 chatbot
```

## Structure
- `src/nlp`: Core NLP components (Intent, Retrieval, Translation).
- `src/api.py`: FastAPI backend.
- `static`: Frontend assets.
