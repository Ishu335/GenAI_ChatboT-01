# 🌟 GenAI ChatBot (React + FastAPI)

A **GenAI-style AI Chat Application** built with **React (Frontend)** and **FastAPI (Backend)**.  
This project demonstrates AI-powered chat functionality combined with **secure backend data storage using Firebase**.  
It includes an **automatic setup script (`install.bat`)** for easy installation on Windows.

---

## 🚀 Features

- 🧠 AI-powered chat using FastAPI backend  
- 🔥 **Realtime data storage** with Firebase Firestore  
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
- **CSS** for styling  

### Backend
- **FastAPI** for serving AI responses  
- **Python** for API handling  
- **Uvicorn** for local server  
- **Firebase Admin SDK** for Firestore integration  
- **dotenv** for environment variable management  

---

## 📁 Project Structure

```
genai-project/
├── backend/
│   ├─ routers/
│   │  ├── database.py        # Firebase Connection
│   │  ├── firebase_config.py # Firebase Admin SDK setup
│   │  └── promt_send.py      # Message send
│   ├── main.py              # FastAPI backend entry   
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # API key stored here
│   ├── genai-chatbot.json   # JSON file
│   └── pycache/
|
├── src/
│   ├── components/          # Chat, Sidebar, MessageBubble, etc.
│   ├── App.jsx              # Main React component
│   ├── main.jsx             # React entry point
│   ├── index.css            # Global CSS
│   └── api/axios.js         # Axios configuration for backend API
│
├── package.json
├── vite.config.js
├── .env                     # Frontend API URL (optional)
├── install.bat              # Automatic installer for Windows
├── dockerfile               # (Optional) for containerization
└── README.md
```

---

## 🔄 How It Works

- The React frontend captures user input.  
- It sends a POST request to the FastAPI backend.  
- The backend processes the request using your AI API key and **stores project data or chat messages in Firebase Firestore**.  
- The frontend displays the AI-generated response in the chat UI.  

---

## ⚙️ Quick Start (Windows Users)

### ▶️ Step 1: Run the Installer

Double-click the file:

**install.bat**

This script will automatically run the project:
1. Create a virtual environment for the backend  
2. Install backend dependencies (`FastAPI`, `Uvicorn`, `firebase-admin`, etc.)  
3. Install frontend dependencies (`npm install`)  
4. Start both servers — backend (FastAPI) and frontend (React)  

After a few moments, your **GenAI Chatbot app** will be running!  

---

## Screenshot
<img src="https://github.com/Ishu335/gemini-clone/blob/master/Images/Gemini%201.png" alt="GenAI Chatbot" />
