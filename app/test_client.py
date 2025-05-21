import asyncio
import websockets
import sys

async def test_client(room_id, user_id):
    uri = f"ws://localhost:8000/ws/{room_id}/{user_id}"
    async with websockets.connect(uri) as websocket:
        # 메시지 수신 스레드
        async def receive():
            while True:
                message = await websocket.recv()
                print(f"수신: {message}")
        asyncio.create_task(receive())

        # 메시지 전송
        while True:
            msg = input("메시지 입력: ")
            await websocket.send(msg)

# 명령줄 인자로 room_id와 user_id 받기
if __name__ == "__main__":
    room_id = sys.argv[1] if len(sys.argv) > 1 else "room1"
    user_id = sys.argv[2] if len(sys.argv) > 2 else "user1"
    asyncio.run(test_client(room_id, user_id))