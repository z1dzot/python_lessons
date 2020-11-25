# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


month_number = int(input('Введите номер месяца: '))
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

while month_number < 1:
    print('Введите значение от 1 до 12!')
    month_number = int(input('Введите номер месяца: '))
if month_number > 12:
    print('Введите значение от 1 до 12!')
    month_number = int(input('Введите номер месяца: '))

for key in seasons.keys():
    if month_number in seasons[key]:
        print(key)





