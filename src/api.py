from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import json
from .chatbot import ChatbotEngine
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAQ_PATH = os.path.join(BASE_DIR, 'data', 'faqs.json')
bot = ChatbotEngine(FAQ_PATH)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    with open(os.path.join(BASE_DIR, 'static', 'index.html')) as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response_data = bot.process_message(data)

            await websocket.send_json(response_data)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close()
