from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from LLM.model.model import general_purpose_model
from tools.tools import search
from llm.model import coding_model,general_purpose_model

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



general_llm = general_purpose_model()



class Prompt(BaseModel):
    prompt: str
    model: str = "general"


@app.post("/send/prompt")
async def generate(request: Prompt):

    user_prompt = request.prompt
    search_responce=search(user_prompt)
   
    response = general_llm.invoke(f"This is user Prompt : {user_prompt} Use this information to generated meaninfull information for user {search_responce}")
    return {
        "response": response,
        "model": request.model
    }

