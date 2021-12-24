from core.dbmanager import get_meaning
from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.get("/hamsang")
def get_countries():

    json_data = json.loads(request.get_data())

    word = json_data['word']
    table = json_data['table']
    meaning = get_meaning(word, table, json_out=False)
    result = {
        "success": "true",
        "message": "Here is what you want",
        "data": [
            {"table":table,
            'words': meaning}]
    }


    return jsonify(result)
