# The else statement will be call when break statement won't be reach
data = [4,6,7,8,1,2,4,5,3,9,8]
for element in data:
    if element == 10:
        break
else:
    print('Break statement wasn\'t reach')