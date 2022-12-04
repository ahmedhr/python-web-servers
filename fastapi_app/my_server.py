import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return "reached Fast API"


if __name__ == "__main__":
    uvicorn.run("my_server:app", port=5002, log_level="info")
