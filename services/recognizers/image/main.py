from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn

app = FastAPI()

@app.post("/")
def predict_image():
    pass