from sys import argv

name, production, bet, bonus = argv


def salary():
    return (int(production) * int(bet)) + int(bonus)


print(salary())
