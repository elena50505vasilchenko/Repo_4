def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr


num = 1
for el in fact(int(input())):
    print(f"Факториал числа {num} равен {el}")
    num += 1
