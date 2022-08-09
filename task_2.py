lst_1 = []
lst = [int(i) for i in input("Введите числа в одну строку через пробел: ").split()]
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        (lst_1.append(lst[i]))

print("Элементы списка, которые больше предыдущего: ", lst_1)