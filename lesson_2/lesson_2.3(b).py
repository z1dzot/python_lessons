# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


month_number = int(input('Введите номер месяца: '))
seasons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while month_number < 1:
    print('Введите значение от 1 до 12!')
    month_number = int(input('Введите номер месяца: '))
    continue
if month_number > 12:
    print('Введите значение от 1 до 12!')
    month_number = int(input('Введите номер месяца: '))

while month_number in seasons:
    if month_number in [12, 1, 2]:
        print('Это Зима!')
        break
    elif month_number in [3, 4, 5]:
        print('Это Весна!')
        break
    elif month_number in [6, 7, 8]:
        print('Это Лето!')
        break
    else:
        print('Это Осень!')
        break


