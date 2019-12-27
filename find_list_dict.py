# Find an item in a list of dictionaries.

data = [
    {
        'name': 'Jhon',
        'age': 25
    },
    {
        'name': 'Carl',
        'age': 18,        
    },
    {
        'name': 'Irene',
        'age': 21
    }
]

print(list(filter(lambda item: item['age'] == 18,data)))  
# [{'name': 'Carl', 'age': 18}]