# gemini_integration.py
import os
from google import generativeai as genai
from google.generativeai import types
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# IMPORTANT: Do NOT hardcode your API key directly in client-side code or scripts
# intended for production. This is for demonstration purposes only.
# In a real application, fetch this securely from environment variables or a backend.
API_KEY = "AIzaSyDXSr6Fi4CmVgtAqbhsq4mSyV7IslD8sso" # Replace with your actual API key
MODEL_NAME = "gemini-1.5-pro" # Matches the model in gemini.js

async def run_chat(prompt: str) -> str:
    """
    Connects to the Gemini API, sends a prompt, and returns the response.
    Mirrors the functionality of runChat in gemini.js.
    """
    try:
        genai.configure(api_key=API_KEY)

        generation_config = types.GenerationConfig(
            temperature=0.9,
            top_k=1,
            top_p=1,
            max_output_tokens=2048,
        )

        safety_settings = [
            {
                "category": HarmCategory.HARM_CATEGORY_HARASSMENT,
                "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            {
                "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            {
                "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            {
                "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
        ]

        # Pass generation_config and safety_settings to the GenerativeModel constructor
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        chat = model.start_chat(
            history=[], # Similar to gemini.js, you can add previous messages here
        )

        print("Sending prompt:", prompt) # Log the prompt for debugging
        response = await chat.send_message(prompt)
        response_text = response.text
        print("Received response:", response_text) # Log the response for debugging

        return response_text
    except Exception as e:
        print(f"Error running chat with Gemini API: {e}")
        raise e

async def main():
    """
    Example of how to use run_chat. In a real application, this would be
    triggered by an API endpoint call from the frontend.
    """
    try:
        response = await run_chat("what is react js")
        print("\nInitial AI Response (from simulated Context.jsx useEffect):")
        print(response)

        response_two = await run_chat("Explain asynchronous programming in Python.")
        print("\nSecond AI Response:")
        print(response_two)

    except Exception as e:
        if "429" in str(e):
            print("You have exceeded your Gemini API quota. Please try again later.")
        else:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())