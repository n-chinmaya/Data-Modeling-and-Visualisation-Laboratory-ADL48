try:
    a = 20 / 0
except ZeroDivisionError:
    print("division by 0 not allowed")

try:
    print(a)
except NameError:
    print("Name error")

try:
    i = [1, 2, 3]
    print(i[49])
except IndexError:
    print("Index error")

try:
    d = {'a': 1, 'b': 2}
    print(d['f'])
except KeyError:
    print("Key Error")

print("\nAll exceptions handled successfully!")