from typing import List

class ChatRoom:
    def __init__(self):
        self.room_id = room_id
        self.users = [] # 접속한 유저 목록
        self.messages = [] # 메시지 기록

class Message:
    def __init__(self, sender: str, content: str):
        self.sender = sender
        self.content = content