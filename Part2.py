
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
print (set(list_a) & set(list_b))

for x in list_a:
    if (x not in list_b):
        print(x)

for y in list_b:
    if (y not in list_a):
        print(y)
