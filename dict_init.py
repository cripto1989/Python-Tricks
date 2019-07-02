# 3 ways to init a dict

# Using curly braces directly
music = {
    'title': 'I started the joke',
    'author' 'Bee Gees'
    'duration_seconds': 350
}

# Using dict constructor and tuples
song = dict([
    ("title","It's my life"),
    ("singer", "Dr. Alban"),
    ("duration_seconds", 350)
])

# Using dict constructor and only params
last = dict(title='It\'s my life', singer='Dr Alban', duration_seconds=350)