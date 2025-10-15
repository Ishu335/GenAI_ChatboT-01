@echo off
echo ===========================================
echo 🚀 Starting Project (FastAPI + React)
echo ===========================================

REM === Step 1: Create virtual environment if not exists ===
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
) else (
    echo Virtual environment already exists.
)
REM === Step 2: Activate virtual environment ===
call .venv\Scripts\Activate.ps1
echo ✅ Virtual environment activated.


REM === Step 3: Install backend dependencies ===
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
)

REM === Step 4: Go to backend folder ===
cd backend

REM === Step 5: Start FastAPI backend in a new terminal ===
echo Starting FastAPI backend on http://127.0.0.1:8000 ...
start cmd /k "call ..\.venv\Scripts\activate && uvicorn main:app --reload --port 8000"

REM === Step 6: Go to frontend and start React ===
cd ..
echo Starting React frontend on http://127.0.0.1:5173 ...
start cmd /k "npm run dev"

echo ===========================================
echo ✅ Both backend and frontend are starting!
echo Backend: http://127.0.0.1:8000
echo Frontend: http://127.0.0.1:5173
echo ===========================================
