from fastapi import FastAPI
from fastapi import status




app = FastAPI()


@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/Health")
async def statusof ():
    return {"status":"ok"}

