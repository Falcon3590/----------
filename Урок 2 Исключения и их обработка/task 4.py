# Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

num = input("Введите значение: ")
try:
    if num == "":
        raise ValueError("введена пустая строка")
    else:
        print(num)
except ValueError as e:
    print(e)
