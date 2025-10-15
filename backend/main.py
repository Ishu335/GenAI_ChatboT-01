import base64
import mimetypes
from pydantic import BaseModel
from google import genai
from google.genai import types
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware  #enable the cross object resourse sources

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

API_KEY = "AIzaSyAnA0h_y57Stbf-haSF_UwSzLn7MLxD7SQ" # Replace with your key
client = genai.Client(api_key=API_KEY)

class Prompt(BaseModel):
    prompt: str


def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"✅ File saved: {file_name}")

@app.post("/send/prompt")
async def generate(request: Prompt):
    try:
        # ✅ Extract string value
        user_prompt = str(request.prompt)

        # ✅ Prepare model input
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_prompt)]
            )
        ]

        # ✅ Generation config
        config = types.GenerateContentConfig(response_modalities=["TEXT"])

        # ✅ Generate response
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=config,
        )

        return {"response": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

