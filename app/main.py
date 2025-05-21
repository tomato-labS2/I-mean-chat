from fastapi import FastAPI
from .api.chat import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# app = FastAPI()
# app.include_router(chat.router, prefix="/chat")
