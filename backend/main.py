from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD

from LLM.model.model import general_purpose_model
from tools.tools import search

=======
from llm.model import coding_model,general_purpose_model
>>>>>>> 5f324a17e5cfa6a4df6c2a32f3bc067208cd9dbd
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


<<<<<<< HEAD

general_llm = general_purpose_model()

=======
>>>>>>> 5f324a17e5cfa6a4df6c2a32f3bc067208cd9dbd

class Prompt(BaseModel):
    prompt: str
    model: str = "general"


@app.post("/send/prompt")
async def generate(request: Prompt):

    user_prompt = request.prompt
<<<<<<< HEAD
    search_responce=search(user_prompt)
   
    response = general_llm.invoke(f"This is user Prompt : {user_prompt} Use this information to generated meaninfull information for user {search_responce}")
    return {
        "response": response,
        "model": request.model
    }
=======

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



>>>>>>> 5f324a17e5cfa6a4df6c2a32f3bc067208cd9dbd
