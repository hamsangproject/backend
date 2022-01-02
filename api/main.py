from typing import Optional
from fastapi import FastAPI
from core.dbmanager import get_meaning


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/v0/word/{word}")
def get_term_from_all_dic(word: str):
    output = get_meaning(word, '*')
    result = {
        "success": "true",
        "message": "Here is what you want",
        "data": output
    }

    return result
