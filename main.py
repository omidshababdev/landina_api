from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from account.config import settings
import uvicorn

from account.routers import auth, user
# from services.monitor.brandwidth import main

account = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:account", host="127.0.0.1", port=5000, reload=True)

account = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

account.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ROUTES
@account.get("/")
async def root():
    return {"message": "Welcome to Landina API"}

## ACCOUNT
account.include_router(auth.router, tags=['Auth'], prefix='/auth')
account.include_router(user.router, tags=['Users'], prefix='/users')

## MONITORS
# account.include_router(main.router, tags=['Monitors'], prefix='/monitors')