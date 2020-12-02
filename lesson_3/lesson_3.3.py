# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_function(*args):
    return sum(args) - min(args)


print(my_function(1, 2, 5))

