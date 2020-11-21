"""Спортсмен занимается ежедневными пробежками. В первый день его результат
составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который общий
результат спортсмена составить не менее b километров. Программа должна
принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22"""

a = int(input("Введите результат пробежки первого дня: "))
b = int(input("Введите общий желаемый результат в км: "))

result_days = 1
result_km = a

while result_km < b:
    a = a + a * 0.1
    result_days += 1
    result_km = result_km + a
    print("%.2f" % a)

print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
