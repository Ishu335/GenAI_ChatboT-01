# 🌟 GenAI LLM Chat Application

A **GenAI-powered chat application** built with **React, FastAPI, LangChain, Hugging Face Transformers, and a local instruction-tuned LLM**.

The application provides a modern chat interface where users can submit prompts and receive AI-generated responses through a FastAPI backend. The backend integrates the **Qwen2.5-1.5B-Instruct** model using Hugging Face Transformers and LangChain's `HuggingFacePipeline`.

---

## 🚀 Features

- 🧠 **LLM-powered text generation**
- 🤗 **Qwen2.5-1.5B-Instruct** integration
- 🔗 **LangChain + HuggingFacePipeline** integration
- ⚡ FastAPI REST API for LLM inference
- ⚛️ React + Vite frontend
- 🔄 Frontend-to-backend API communication using Axios
- 🧩 Modular LLM architecture
- 📱 Responsive chat interface
- 🎨 Modern UI inspired by AI chat applications
- 🔐 Environment-based configuration
- 🖥️ Local LLM inference without requiring an external AI API

---

## 🛠 Tech Stack

### Frontend

- **React.js**
- **Vite**
- **Axios**
- **JavaScript**
- **CSS**

### Backend

- **Python**
- **FastAPI**
- **Uvicorn**
- **LangChain**
- **LangChain Hugging Face**
- **Hugging Face Transformers**
- **PyTorch**

### LLM

- **Qwen2.5-1.5B-Instruct**
- **Text Generation Pipeline**
- **HuggingFacePipeline**

### Development Tools

- **Git**
- **GitHub**
- **Python Virtual Environment**
- **VS Code**

---

## 🏗️ Architecture

```text
┌─────────────────────────────┐
│       React + Vite          │
│                             │
│     Chat User Interface     │
└──────────────┬──────────────┘
               │
               │ HTTP POST
               ▼
┌─────────────────────────────┐
│          FastAPI            │
│                             │
│       REST API Layer        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│         LangChain           │
│                             │
│     HuggingFacePipeline     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Hugging Face             │
│       Transformers          │
│                             │
│ Qwen2.5-1.5B-Instruct       │
└──────────────┬──────────────┘
               │
               ▼
        Generated Response
```

---

## 📁 Project Structure

```text
GenAI_ChatboT-01/
│
├── backend/
│   │
│   ├── LLM/
│   │   └── model/
│   │       └── model.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── src/
│   ├── components/
│   │   ├── Chat/
│   │   ├── Sidebar/
│   │   └── MessageBubble/
│   │
│   ├── App.jsx
│   ├── Main.jsx
│   ├── Main.css
│   ├── index.css
│   │
│   └── api/
│       └── axios.js
│
├── public/
│
├── package.json
├── vite.config.js
├── install.bat
├── Dockerfile
└── README.md
```

---

## 🧠 LLM Implementation

The backend uses Hugging Face Transformers to load the Qwen instruction-tuned model.

```python
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline


def general_purpose_model():

    general_pipe = pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-1.5B-Instruct",
        device=-1,
        max_new_tokens=256,
    )

    return HuggingFacePipeline(
        pipeline=general_pipe
    )
```

The Transformers pipeline is then exposed to the application through LangChain's `HuggingFacePipeline`.

---

## 🔄 How It Works

1. The user enters a prompt in the React chat interface.
2. React sends the prompt to the FastAPI backend.
3. FastAPI receives the request through a REST endpoint.
4. LangChain passes the prompt to the Hugging Face pipeline.
5. The Qwen2.5-1.5B-Instruct model generates the response.
6. FastAPI returns the generated response as JSON.
7. React displays the response in the chat interface.

```text
User
 ↓
React UI
 ↓
Axios
 ↓
FastAPI
 ↓
LangChain
 ↓
HuggingFacePipeline
 ↓
Qwen2.5-1.5B-Instruct
 ↓
Generated Text
 ↓
FastAPI
 ↓
React UI
```

---

## ⚙️ API Endpoint

### Generate Response

```http
POST /send/prompt
```

### Request

```json
{
  "prompt": "Explain FastAPI in simple terms"
}
```

### Response

```json
{
  "response": "FastAPI is a modern Python framework..."
}
```

---

## ⚙️ Installation

### Prerequisites

Make sure you have installed:

- Python 3.11 recommended
- Node.js
- npm
- Git

---

### Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main:app --reload --port 8000
```

Backend will run at:

```text
http://127.0.0.1:8000
```

---

### Frontend Setup

From the project root:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

Frontend will normally run at:

```text
http://localhost:5173
```

---

## 🪟 Windows Quick Start

The project includes:

```text
install.bat
```

The script can be used to automate environment setup, dependency installation, and application startup.

---

## 🔮 Future Improvements

The project architecture can be extended with:

- 🤖 Specialized coding LLM using **DeepSeek Coder**
- 🔀 Automatic model routing
- 🦜 LangGraph-based workflows
- 📚 Retrieval-Augmented Generation (RAG)
- 🔎 Vector search
- 🧠 Conversation history
- 📄 PDF/document question answering
- 🛠️ LLM tool calling
- 🐳 Docker deployment
- ☁️ Cloud deployment

---

## 📸 Screenshot

<img src="https://github.com/Ishu335/gemini-clone/blob/master/Images/Gemini%201.png" alt="GenAI LLM Chat Application" />

---

## 👨‍💻 Author

**Ishwar Sonawane**

GitHub: [Ishu335](https://github.com/Ishu335)

---

## 📌 Project Highlights

**GenAI | LLM | LangChain | Hugging Face | Transformers | Qwen | FastAPI | React | Vite | Python**
