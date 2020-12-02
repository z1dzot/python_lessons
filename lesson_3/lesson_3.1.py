# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def function(var1, var2):
    try:
        return var1 / var2
    except ZeroDivisionError as err:
        print("Error: ", err)


print(function(int(input("Enter var1 = ")), int(input("Enter var2 = "))))
