# Way to replace the traditional comparison of "num > init and num < end"

init = 2 
end = 10
num = 5

print(init < num < end)
# True

print(init <= num <= end)
# True

num = 15
print(init < num < end)
# False
