# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(work_per_hours, state, rate):
    try:
        work_per_hours * state + rate
    except ValueError as err:
        print('Error: ', err)


print(f'Salary - {salary(*map(int, argv[1:]))}')
