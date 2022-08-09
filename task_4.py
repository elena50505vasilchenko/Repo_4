my_list = list(map(int, input("Введите числа в одну строку через пробел: ").split()))
new_list = [i for i in my_list if my_list.count(i) < 2]
print("Числа в единственном экземпляре:", new_list)
