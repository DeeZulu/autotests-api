import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"сообщение: {message}")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f"ответ от сервера: {response}")

asyncio.run(client())