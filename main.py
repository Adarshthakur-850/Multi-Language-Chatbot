import uvicorn
import os

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')

    print("Starting Multi-Language Chatbot Server...")
    print("Open http://localhost:8000 in your browser.")

    uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=False)
