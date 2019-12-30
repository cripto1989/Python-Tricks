groupA = {
    'Messi': 10,
    'Cristiano': 10
}

groupB = {
    'Neynmar': 8,
    'Suarez': 8,
}

# Joining
together = {**groupA, **groupB}
print(together)
together = dict(groupA.items() | groupB.items())
print(together)
# Updating a dict with another
groupA.update(groupB)
print(groupA)