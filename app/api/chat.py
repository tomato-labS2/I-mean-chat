from fastapi import APIRouter, WebSocket
from ..services.chat_service import ChatService
from models.chat_dto import Message

chat_service = ChatService()
router = APIRouter()

@router.websocket("/ws/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, user_id: str):
    await websocket.accept()

    # 채팅방이 없으면 생성
    if not chat_service.repository.get_room(room_id):
        chat_service.create_room(room_id)

    # 유저 추가
    await chat_service.add_user(room_id, user_id, websocket)

    try:
        while True:
            # 클라이언트로부터 메시지 수신
            data = await websocket.receive_text()
            message = Message(user_id, data)
            await chat_service.broadcast(room_id, message)
    except Exception as e:
        # 연결이 끊기면 유저 제거(간단히 생략 가능)
        pass


@router.get("/test")
def hello():
    return {"message": "FastAPI 서버 연결 성공!"}
