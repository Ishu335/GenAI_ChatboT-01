# app.py (a simple Flask server)
import sys
import os
from flask import Flask, request, jsonify
from flask_cors import CORS # To handle CORS issues
import asyncio # Import asyncio for async functions

# Add the parent directory (src) to the Python path
# This assumes app.py is in src/context/ and gemini_integration.py is in src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gemini_integration import run_chat # Now it should be able to find it

app = Flask(__name__)
CORS(app) # Enable CORS for all origins (adjust for production)

# New root route for GET requests
@app.route('/', methods=['GET'])
def home():
    return "Gemini Clone Backend is Running!"

@app.route('/ask_gemini', methods=['POST'])
async def ask_gemini():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response_text = await run_chat(prompt)
        return jsonify({"response": response_text})
    except Exception as e:
        # Improved error handling for 429 specifically
        if "429" in str(e):
            return jsonify({"error": "You have exceeded your Gemini API quota. Please try again later."}), 429
        print(f"Backend Error: {e}")
        return jsonify({"error": f"Failed to get response from Gemini: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app asynchronously
    app.run(debug=True, port=5000) # You can change the port