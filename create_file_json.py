"""
We can create json files using json.dump method for serialize data.
"""
import json
my_book = {"title": "Ana Frank Dairy", "author": "Ana Frank", "number_pages": 340}

with open('book.json','w') as file:
    json.dump(my_book, file, sort_keys=True, indent=4)