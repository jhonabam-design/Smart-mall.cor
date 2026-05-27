
        from fastapi import FastAPI
from ai import ask_ai

app = FastAPI()

# SmartMall products database
products = [
    {
        "id": 1,
        "name": "Hikvision 2MP Turbo HD Camera",
        "price": "650 GHS",
        "stock": 8
    },
    {
        "id": 2,
        "name": "iPhone 13",
        "price": "5200 GHS",
        "stock": 4
    },
    {
        "id": 3,
        "name": "Nike Air Force",
        "price": "450 GHS",
        "stock": 12
    }
]

@app.get("/")
def home():
    return {"status": "SmartMall API running"}

@app.get("/chat")
def chat(message: str):
    try:
        reply = ask_ai(message)
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}

@app.get("/products")
def get_products():
    return products
