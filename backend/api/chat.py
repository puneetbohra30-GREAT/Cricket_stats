from fastapi import APIRouter

router = APIRouter()

@router.post("/")   # endpoint
async def chat(data: dict):
    message = data.get("message", "")

    if "virat" in message.lower():
        reply = "Virat Kohli is one of the best batsmen 🔥"
    elif "dhoni" in message.lower():
        reply = "MS Dhoni is the best finisher 🧠"
    else:
        reply = f"You said: {message}"

    return {
        "response": reply   # ✅ IMPORTANT (was 'reply')
    }