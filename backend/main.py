from fastapi import FastAPI
app=FastAPI()

@app.get('/home')
def def home():
    return  