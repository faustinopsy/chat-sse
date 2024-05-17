from fastapi import APIRouter
from starlette.responses import StreamingResponse
import json
import asyncio
from models.message import Message
from database.database import insert_message, get_new_messages

router = APIRouter()

@router.post("/send_message/")
async def send_message(message_body: Message):
    print(message_body)
    await insert_message(message_body.message,message_body.usuario)
    return {"message": "mensagem enviada."}

async def event_generator():
    last_id = 0
    while True:
        new_messages = await get_new_messages(last_id)
        if new_messages:
            for msg in new_messages:
                yield f"data: {json.dumps(msg)}\n\n"
                last_id = msg['id']
        await asyncio.sleep(1)

@router.get("/events/", status_code=200)
async def get_events():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
