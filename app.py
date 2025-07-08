from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Spam Message Detector using Ollama AI")

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.1:8b"

class Message(BaseModel):
    content: str

@app.post("/check-spam/")
async def check_spam(message: Message):
    prompt = f"""
    You are a spam detection AI. Classify the following message as either "Spam" or "Not Spam" and explain briefly.

    Message: "{message.content}"

    Respond in this exact format:
    Classification: <Spam or Not Spam>
    Reason: <Short explanation>
    """

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()

        response_text = result.get('response', '').strip()

        return {
            "input_message": message.content,
            "ollama_response": response_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Ollama: {str(e)}")

