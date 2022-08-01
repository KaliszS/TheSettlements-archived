from fastapi import FastAPI
from app.src import board

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(board.router, prefix="/board", tags=["Board"])
