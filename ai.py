import requests
import os

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

import requests
import os

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def ask_ai(message):
    try:
        url = "https://api.mistral.ai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistral-small-latest",
            "messages": [
                {
                    "role": "system",
                    "content": "You are SmartMall, an AI assistant for African businesses."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        # 🔥 DEBUG IMPORTANT
        if "choices" not in data:
            return f"API Error: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}":
    try:
        url = "https://api.mistral.ai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistral-small-latest",
            "messages": [
                {"role": "system", "content": "You are SmartMall assistant."},
                {"role": "user", "content": message}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"
