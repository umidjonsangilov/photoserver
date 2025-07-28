# FastAPI Media Host 🎯

Bu oddiy va himoyalangan media server — siz rasm yuklash, ro‘yxatini ko‘rish, va o‘chirish amallarini bajarishingiz mumkin. Barcha jarayon Telegram bot orqali loglanadi.

## 🚀 Boshlanish

### 1. Klonlab oling

```bash
git clone https://github.com/username/fastapi-media-host.git
cd fastapi-media-host
```
### 2. .env faylini tayyorlang
```bash
cp .env.example .env
```
va .env fayl ichiga BOT_TOKEN, CHAT_ID va SECRET_TOKEN kiriting

Bu yerda BOT_TOKEN - harakat haqida ma'lumot yuborish uchun bot tokeni.
         CHAT_ID - sizning telegram idingiz bot sizga xabar yubora oladigan.
         SECRET_TOKEN - faqat siz biladigan kalit so'z. 

### 3. Kutubxonalarni o‘rnating
```bash
pip install -r requirements.txt
```
### 4. Serverni ishga tushiring
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
📡 API endpointlar
| Endpoint        | Method | Tavsif                              |
| --------------- | ------ | ----------------------------------- |
| `/upload/image` | POST   | Rasm yuklash (token kerak)          |
| `/delete`       | DELETE | Rasm o‘chirish (token kerak)        |
| `/files`        | GET    | Rasm ro‘yxatini olish (token kerak) |

🔐 Himoya
Barcha endpointlar x-token orqali faqat siz ishlata oladigan tarzda himoyalangan. .env faylida SECRET_TOKEN belgilanadi.
🧾 Misol so‘rov (curl)
```bash
curl -X POST http://localhost:8000/upload/image \
  -H "x-token: your_secret_token_here" \
  -F "image=@rasm.jpg"
```

📬 Telegram loglash
Har bir rasm yuklanganda, o‘chirilganda yoki ro'yxati ko'rilganda sizga Telegram orqali xabar keladi. Agar kerak bo'lmasa koddan bu qismni o'chirib qo'yasiz.

📄 Litsenziya
MIT — istalgancha foydalaning, o‘zgartiring, ulashing.
