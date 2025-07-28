import os
import uuid
import httpx
from fastapi import FastAPI, UploadFile, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

# Konfiguratsiya
MEDIA_DIR = "static/media"
SECRET_TOKEN = os.getenv("SECRET_TOKEN")
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

# Papka yaratish
os.makedirs(MEDIA_DIR, exist_ok=True)

# Statik fayllar (rasmlar)
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

# Tekshirish
def check_token(x_token: str):
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Ruxsat yo'q")

# Log yuborish telegramga (agar kerak bo'lmasa o'chirib q'ying)
async def send_log(message_text):
    async with httpx.AsyncClient() as client:
            await client.post(
                f"https://api.telegram.org/bot{bot_token}/sendMessage",
                data={"chat_id": chat_id, "text": message_text}
            )

@app.post("/upload/image")
async def upload_image(image: UploadFile, x_token: str = Header(default=None)):
    check_token(x_token)
    ext = os.path.splitext(image.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(MEDIA_DIR, filename)
    with open(filepath, "wb") as f:
        content = await image.read()
        f.write(content)
        message_text = f"📸 Yangi rasm yuklandi:\nhttps://sizningdomeningiz.uz/media/{filename}"
        await send_log(message_text)
    return {"url": f"/media/{filename}"}

@app.delete("/delete")
async def delete_image(filename: str, x_token: str = Header(default=None)):
    check_token(x_token)
    file_path = os.path.join(MEDIA_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Fayl yo'q")
    os.remove(file_path)
    await send_log(f"🗑 Rasm {filename} o'chirildi")
    return {"message":f"{filename} o'chirildi ✅"}

@app.get("/files")
async def list_files(x_token: str = Header(default=None)):
    check_token(x_token)
    files = os.listdir(MEDIA_DIR)
    files = [f for f in files if os.path.isfile(os.path.join(MEDIA_DIR, f))]
    await send_log("🧾 Rasmlar ro'yxati olindi")
    return {"files": files}
