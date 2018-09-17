from collections import Counter
data = [1,3,4,5,6,7,8,1,2,4,5,6]

cnt = Counter(data)
cnt.most_common(2)  # It returns a list of tuples: [(1, 2), (4, 2)]
element = cnt.most_common(2)[0][0]  # Element most common
number_times = cnt.most_common(2)[0][0]  # Number of times found