"""  
This script slice a phrase not exceeding a specific number of characters, always 
slice by words not by characters.
"""

text = "THIS IS A TEXT WE ARE GOING TO CUT"
MAX_SIZE = 25
new_text = ''

def cut_phrase(text: str, size: int, three_points: bool):
    global new_text
    for s in text.split(' '):
        if (len(new_text) + len(s)) <= size:    
            new_text += ' {}'.format(s)
        else:
            break        
    if three_points:
        new_text += '...'
    return new_text.strip()

print(cut_phrase(text, MAX_SIZE, True))
