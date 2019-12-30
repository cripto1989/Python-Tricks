import json

data = {"title": "Ana Frank Dairy", "author": "Ana Frank", "number_pages": 340}
print(json.dumps(data, sort_keys=True, indent=4))

"""
Output:
{
    "author": "Ana Frank",
    "number_pages": 340,
    "title": "Ana Frank Dairy"
}
"""