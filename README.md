# 🌟 Gemini Clone (React + FastAPI)

A **Gemini-style AI Chat Application** built with **React (Frontend)** and **FastAPI (Backend)**.  
This project replicates the elegant and responsive UI of Google Gemini, combined with AI text generation using an API key.  
It includes an **automatic setup script (`install.bat`)** for easy installation on Windows.
---

## 🚀 Features

- 🧠 AI-powered chat using FastAPI backend  
- ⚡ Built with React + Vite for lightning-fast UI  
- 🔐 Secure API key integration  
- 🧩 Modular, reusable components  
- 📱 Fully responsive layout  
- 🌈 Clean, modern interface inspired by Google Gemini  

---

## 🛠 Tech Stack

### Frontend
- **React + Vite**
- **Axios** for API requests
- **CSS / TailwindCSS** for styling

### Backend
- **FastAPI** for serving AI responses
- **Python** for API handling
- **Uvicorn** for local server
- **dotenv** for environment variable management

---

## 📁 Project Structure

```
gemini-clone/
├── backend/
│ ├── main.py # FastAPI backend entry
│ ├── requirements.txt # Python dependencies
│ ├── .env # API key stored here
│ └── pycache/
|
│ ├── src/
│ │ ├── components/ # Chat, Sidebar, MessageBubble, etc.
│ │ ├── App.jsx # Main React component
│ │ ├── main.jsx # React entry point
│ │ ├── index.css # Global CSS
│ │ └── api/axios.js # Axios configuration for backend API
│ ├── package.json
│ ├── vite.config.js
│ └── .env # Frontend API URL (optional)
|── requirements.txt
│── install.bat
├── dockerfile # (Optional) for containerization
└── README.md
```

## 🔄 How It Works

- The React frontend captures user input.
- It sends a POST request to the FastAPI backend.
- The backend processes the request using your API key (e.g., Gemini, OpenAI, etc.) and returns AI-generated text.
- The frontend displays the response in the chat UI.

## ⚙️ Quick Start (Windows Users)

### ▶️ Step 1: Run the Installer

Double-click the file:

**install.bat**

This script will automatically:
1. Create a virtual environment for the backend  
2. Install backend dependencies (`FastAPI`, `Uvicorn`, etc.)  
3. Install frontend dependencies (`npm install`)  
4. Start both servers — backend (FastAPI) and frontend (React)

After a few moments, your Gemini Clone app will be running!

---

## Screenshot
<img src="https://github.com/Ishu335/gemini-clone/blob/master/Images/Gemini%201.png" atl="Gemini CLone" ></img>

