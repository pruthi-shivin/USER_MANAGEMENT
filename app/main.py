from fastapi import FastAPI
from app.routers.user_router import router

app = FastAPI(title="GR_Task") #entry point of the app

app.include_router(router)