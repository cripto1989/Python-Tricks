A = [1, 2, 3, 4, 5]
B = [1, 6, 7, 8, 9]
C = [10, 11, 12, 13]

# Elements not repeated
res = list(set(A + B))
print(res)  #  [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = list(set(A + B + C))
print(res)  #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Extend with elements repeated
A.extend(B)
print(A)  #  [1, 2, 3, 4, 5, 1, 6, 7, 8, 9]

