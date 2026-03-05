from fastapi import FastAPI, WebSocket
from backend.runner import run_algorithm

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Algorithm Visualizer API"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_json()

        algorithm = data["algorithm"]
        input_data = data["input"]

        steps = run_algorithm(algorithm, input_data)

        for step in steps:
            await websocket.send_json(step)