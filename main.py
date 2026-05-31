from fastapi import FastAPI,Request 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import ast
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
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




    