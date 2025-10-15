# 🌌 Gemini Clone (React + FastAPI)

A modern full-stack **Gemini Clone** built using **React (frontend)** and **FastAPI (backend)**.  
The project demonstrates seamless API integration using **Axios**, **CORS**, and **RESTful endpoints** — mimicking an AI-chat style application.

---

## 🚀 Features

- ⚛️ **React (Vite)** frontend for fast and responsive UI  
- 🐍 **FastAPI** backend for high-performance API responses  
- 🌐 **Axios** used for frontend-to-backend communication  
- 🔐 **CORS** enabled for cross-origin API access  
- 📦 Modular code structure for scalability  
- 🎨 Clean and responsive chat UI (Gemini-style layout)

---

## 🧰 Tech Stack

| Layer | Technology |
|--------|-------------|
| Frontend | React + Vite + Axios |
| Backend | FastAPI + Uvicorn |
| Styling | CSS / TailwindCSS |
| API Handling | Axios |
| Middleware | CORS |
| Language | JavaScript (Frontend), Python (Backend) |

---

## 📁 Folder Structure
```
gemini-clone/
├── backend/
│ ├── main.py # FastAPI entry point
│── src/
│ │ ├── components/ # Reusable React components
│ │ ├── pages/ # Page components
│ │ ├── services/axios.js # Axios configuration
│ │ ├── App.jsx # Main React app
│ │ └── main.jsx # Entry point
│ ├── package.json
│ └── vite.config.js
│
└── README.md
```

## Expanding the ESLint configuration
<img src="https://github.com/Ishu335/gemini-clone/blob/master/Images/Gemini%201.png" atl="Gemini CLone" ></img>
If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
