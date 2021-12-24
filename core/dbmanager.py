import sqlite3
import json

database_filename = 'core/databases/dics.db'

def _get_meaning_dict(word: str, database: str):
    connection = sqlite3.connect(database_filename)
    table_name = database
    query_text = f'SELECT * FROM {table_name} WHERE word IS \'{word}\';'
    query_result = connection.execute(query_text)
    output = []
    for result in query_result:
        result_dict = {'id': result[0],
                       'word': result[1],
                       'definition': result[2],
                       'context': result[3],
                       }
        output.append(result_dict)
    
    return output


def get_meaning(word: str, database: str, json_out: bool = False):
    if json_out == True:
        return json.dumps(_get_meaning_dict(word, database), ensure_ascii=False, indent=1)
    else:
        return _get_meaning_dict(word, database)
