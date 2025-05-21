from app.models.chat_dto import ChatRoom, Message


class ChatRepository:
    # __init__ : 파이썬 클래스의 생성자. 클래스의 객체가 만들어 질 때 자동으로 호출돼서 초기화를 담당한다.
    # 메서드명(self) : self 는 자바의 this 와 같은 개념이며 클래스의 인스턴스 자신을 가르킨다. 파이썬에서는 메서드 정의할 때 첫번째 매개변수로 self 를 명시적으로 작성해야한다.
    def __init__(self):
        self.rooms = {} # 채팅방을 저장할 메모리 DB (딕셔너리)
        # 이 클래스의 멤버 변수를 정의. 자바로 치면 private Map<String, ChatRoom> rooms 같은 느낌
        # {} : 파이썬의 딕셔너리를 의미. 자바의 HashMap 과 비슷한 자료구조로 키-값 쌍으로 데이터를 저장한다.
        # self.rooms 는 채팅방 데이터를 저장하는 빈 딕셔너리를 만드는 것이다. 나중에 채팅방을 추가하면 {room_id : ChatRoom 객체} 형태로 저장된다.

    # room_id: str -> room_id 는 매개변수, str는 타입 힌트. 매개변수는 문자열 타입이어야 한다는 뜻이다.
    # -> ChatRoom: -> 메서드가 반환하는 값의 타입 힌트. 이 메서드는 ChatRoom 객체를 반환한다는 뜻이다.
    def create_room(self, room_id: int) -> ChatRoom:
        room = ChatRoom(room_id) # ChatRoom 클래스의 객체 생성. 자바로 치면 ChatRoom room = new ChatRoom(room_id); 같은 코드드
        self.rooms[room_id] = room # 앞에서 __init__ 에서 만든 딕셔너리 변수에 키로 room_id 를 사용. 자바로 치면 rooms.put(room_id, room)
        return room
    
    def get_room(self, room_id: int) -> ChatRoom:
        return self.rooms.get(room_id)
    
    def add_user_to_room(self, room_id: int, user_id: str):
        room = self.get_room(room_id)
        if room and user_id not in room.users:
            room.users.append(user_id)

    def add_message(self, room_id: int, message: Message):
        room = self.get_room(room_id)
        if room:
            room.messages.append(message)