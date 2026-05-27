from fastapi import FastAPI
from ai import ask_ai

app = FastAPI()

@app.get("/")
def home():
    return {"status": "SmartMall API running"}

@app.get("/chat")
def chat(message: str):
    reply = ask_ai(message)
    return {"reply": reply}
@app.get("/send")
def send(message: str):
    reply = ask_ai(message)
    return {
        "from": "SmartMall",
        "to": "customer",
        "message_received": message,
        "reply": reply
    }
products = [
    {
        "id": 1,
        "name": "Nike Air",
        "price": 450,
        "stock": 12
    },
    {
        "id": 2,
        "name": "iPhone 13",
        "price": 5200,
        "stock": 4
    }
]

@app.get("/products")
def get_products():
    return products
