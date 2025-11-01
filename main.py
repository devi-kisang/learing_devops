from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello, DEVOPS!!!!!"}

@app.get("/status")
async def status():
    return{"status":"200","msg":"working"}