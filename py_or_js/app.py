from fastapi import FastAPI , UploadFile

app = FastAPI()

@app.get('/')
def home():
    return { 'data':"welcome to home page"}

@app.get('/contact')
def home():
    return { 'data':"welcome to contact page"}

@app.post("/upload")
def handleImage(files:list[UploadFile]):
    print(files)
    return {"status":"files uploaded"}

import uvicorn
uvicorn.run(app)