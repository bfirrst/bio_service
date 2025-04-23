from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
import os

class BioRequest(BaseModel):
    session_file: str  # without ".session"
    api_id: int
    api_hash: str
    username: str

app = FastAPI()

@app.post("/bio")
async def get_bio(req: BioRequest):
    session_path = os.path.join("sessions", req.session_file)
    if not os.path.exists(session_path + ".session"):
        raise HTTPException(status_code=404, detail="Session file not found")
    try:
        client = TelegramClient(session_path, req.api_id, req.api_hash)
        await client.connect()
        entity = await client.get_entity(req.username)
        full = await client(GetFullUserRequest(entity))
        bio = full.full_user.about or ""
        await client.disconnect()
        return {"bio": bio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
