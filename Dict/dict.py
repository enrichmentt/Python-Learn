d = {'A': 12, 'B': 1, 'D': 19, 'E': 22}

for key in d:
    print(key, end=' ')
print()
for key in d.keys():
    print(key, end=' ')
print()
for value in d.values():
    print(value, end=' ')
print()
for key, item in d.items():
    print(key, "-", item, end=' ')
