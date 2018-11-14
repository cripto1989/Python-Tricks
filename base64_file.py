import base64

img = b'base64_file_string'

with open("name_image.png", "wb") as file:
    file.write(base64.decodebytes(img))