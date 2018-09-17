data = {
    'mac_os': 18,
    'windows': 15,
    'linux': 25,
    'chrome_os': 12
}
list_data = sorted(data.items(), key=lambda x: x[1])
print(list_data)  # Output: [('chrome_os', 12), ('windows', 15), ('mac_os', 18), ('linux', 25)]
smaller = list_data[0]
bigger = list_data[::-1][0]
print(smaller)  # ('chrome_os', 12)
print(bigger)  # ('linux', 25)