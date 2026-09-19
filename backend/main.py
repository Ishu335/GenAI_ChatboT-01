from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load model ONCE when FastAPI starts
pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen3-0.6B",
    device_map="auto"
)


class Prompt(BaseModel):
    prompt: str


@app.post("/send/prompt")
async def generate(request: Prompt):

    user_prompt = request.prompt

    messages = [
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    result = pipe(
        messages,
        max_new_tokens=100
    )

    return {
        "response": result[0]["generated_text"][-1]["content"]
    }