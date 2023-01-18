from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
import uvicorn

from app.routers import auth, user

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ROUTES
@app.get("/")
async def root():
    return {"message": "Welcome to Landina API"}

app.include_router(auth.router, tags=['Auth'], prefix='/auth')
app.include_router(user.router, tags=['Users'], prefix='/users')

