# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce


def multiply(arg1, arg2):
    return arg1 * arg2


my_list = [el for el in range(100, 1001, 2)]
print(f'{reduce(multiply, my_list)}')
