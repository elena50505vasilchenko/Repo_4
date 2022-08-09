from functools import reduce
lst = [i for i in range(100, 1001) if i % 2 == 0]
print("Сформированный список:", lst)


def my_func(el_1, el_2):
    return el_1 * el_2


print("Произведение чисел списка:", reduce(my_func, lst))
