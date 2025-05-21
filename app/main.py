from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.chat import router
import typing

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 ["http://localhost", "http://localhost:8000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def print_all_routes():
    print("▶▶▶ 등록된 라우트:")
    for r in app.router.routes:
        # WebSocketRoute는 WebSocket 전용 라우트입니다.
        print(type(r).__name__, r.path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# app = FastAPI()

# app.include_router(chat.router, prefix="/chat")
