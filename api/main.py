from typing import Optional
from fastapi import FastAPI
from core.dbmanager import get_meaning


app = FastAPI()



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
