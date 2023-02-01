import json
import os
import sys
from settings import CURRENT


def read_json(file_name):
    current = CURRENT
    file_name = 'tests_data.json'
    full_path = os.path.join(current, file_name)
    with open(full_path,  encoding='utf-8') as f:
        book_list = json.load(f)
    return book_list
