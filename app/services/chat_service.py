from services.chat_repository import ChatRepository
from models.chat_dto import Message
import asyncio
# asyncio : async/await 구문을 사용하여 동시성 코드를 작성할 수 있게 해주는 모듈로 단일 스레드 작업을 병렬로 처리할 수 있다.

class ChatService:
    def __init__(self):
        self.repository = ChatRepository
        self.connections = {} # {room_id: {user_id: websocket}} 형태로 웹소켓 저장

    def create_room(self, room_id: int):
        self.repository.create_room(room_id)
        self.connections[room_id] = {}

    async def add_user(self, room_id: int, user_id: str, websocket):
        # 유저를 채팅방에 추가
        self.repository.add_user_to_room(room_id, user_id)
        self.connections[room_id][user_id] = websocket
        
        # 두 명이 접속했는지 확인
        room = self.repository.get_room(room_id)
        if len(room.users) == 2 and "AI" not in room.users:
            # AI 상담사 추가
            self.repository.add_user_to_room(room_id, "AI")
            await self.broadcast(room_id, Message("AI", "안녕하세요! 커플 갈등 해결을 도와드릴 AI 상담사입니다."))

    async def broadcast(self, room_id: int, message: Message):
        # 메시지를 채팅방에 저장
        self.repository.add_message(room_id, message)

        # 모든 참여자에게 메시지 전송
        room_connections = self.connections.get(room_id, {})
        for user_id, websocket in room_connections.items():
            await websocket.send(f"{message.sender}: {message.content}")
