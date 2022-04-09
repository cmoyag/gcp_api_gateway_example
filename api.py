from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/lista")
def lista():
    return{"elemento1":"valor1","elemento2":"valor2","elemento3":"valor3"}    