from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}