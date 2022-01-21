from typing import Optional
from fastapi import FastAPI
from core.dbmanager import get_meaning
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v0/word/{word}")
def get_term_from_all_dic(word: str):
    output = get_meaning(word, '*')
    result = {
        "success": "true",
        "message": "Here is what you want",
        "data": output
    }

    return result

