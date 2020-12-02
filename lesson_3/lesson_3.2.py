# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def info(first_name, last_name, b_year, city, email, phone_number):
    return f'Name: {first_name}\n' \
           f'last_name: {last_name}\n' \
           f'b_year: {b_year}\n' \
           f'city: {city}\n' \
           f'email: {email}\n' \
           f'phone_number: {phone_number}\n'


print(info(first_name= "Arman",
           last_name= "Oganesyan",
           b_year= "03.08.1990",
           city= "Moscow",
           email= "z1dzot@gmail.com",
           phone_number="+123456789"))


