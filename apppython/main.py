from fastapi import FastAPI
from starlette.responses import StreamingResponse
import aiomysql
import json
import asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",  
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root123',
    'db': 'a01_teste',
}

from pydantic import BaseModel

class Message(BaseModel):
    message: str


async def insert_message(message: str):
    async with aiomysql.connect(**DB_CONFIG) as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
            await conn.commit()

async def get_new_messages(last_id: int):
    async with aiomysql.connect(**DB_CONFIG) as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute("SELECT id, message FROM messages WHERE id > %s ORDER BY id ASC", (last_id,))
            result = await cur.fetchall()
            return result

@app.post("/send_message/")
async def send_message(message_body: Message):
    await insert_message(message_body.message)
    return {"message": "Message sent successfully."}

async def event_generator():
    last_id = 0
    while True:
        new_messages = await get_new_messages(last_id)
        if new_messages:
            for msg in new_messages:
                yield f"data: {json.dumps(msg['message'])}\n\n"
                last_id = msg['id']
        await asyncio.sleep(1)

@app.get("/events/", status_code=200)
async def get_events():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
