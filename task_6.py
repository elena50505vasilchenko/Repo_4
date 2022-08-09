from itertools import count, cycle

for i in count(int(input("Введите число: "))):
    if i > 20:
        break
    else:
        print(i)

lst = list(input("Введите значения через пробел: ").split())
counter = 0
for i in cycle(lst):
    if counter > 35 or i == "#":
        break
    print(i)
    counter += 1

