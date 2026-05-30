from fastapi import FastAPI,Request 
from pydantic import BaseModel
import requests
import ast
from openai import OpenAI


app = FastAPI()

client = OpenAI(
    api_key = "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",
    base_url="https://api.groq.com/openai/v1"
)
@app.post("/generate")

async def generate(req:Request):
    data = await req.json()
    p=data["prompt"]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": p
            }
        ]
    )
    answer = response.choices[0].message.content
    return {
        "object": answer
    }




    