from fastapi import FastAPI
from config import ORIGINS
from fastapi.middleware.cors import CORSMiddleware
from routes.message_routes import router as message_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(message_router)
