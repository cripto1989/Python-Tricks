data = {
    "hello":"world",
    "here":"there",
    "code": "Python"
}

# Removing just an element
one_delete = {key:value for key,value in data.items() if key not in ["hello"]}
print(one_delete)

# Removing two or more elements
two_more_delete = {key:value for key,value in data.items() if key not in ["hello","here"]}
print(two_more_delete)