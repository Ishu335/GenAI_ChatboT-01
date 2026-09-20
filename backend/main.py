from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llm.model import coding_model,general_purpose_model
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

    if "code" in user_prompt.lower() or "python" in user_prompt.lower():
            response = coding_model().invoke(messages)
    else:
        response = general_purpose_model().invoke(messages)

    
    print("\n\n\n Result: ",response)
    return response
    # return {
    #     "response": result[0]["generated_text"][-1]["content"]
    # }



