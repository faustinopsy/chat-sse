from fastapi import APIRouter
from starlette.responses import StreamingResponse
import json
import asyncio
from models import Message
from database import insert_message, get_new_messages

router = APIRouter()

@router.post("/send_message/")
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

@router.get("/events/", status_code=200)
async def get_events():
    return StreamingResponse(event_generator(), media_type="text/event-stream")