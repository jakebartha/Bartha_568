

a = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
b = []

for item in a:
    if item < 5:
        b.append(item)

print b


a = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
print [item for item in a if item < 5]