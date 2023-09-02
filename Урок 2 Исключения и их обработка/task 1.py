# Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
# и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению
# приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.

def checknum ():
    num = input("Введите дробное число: ")
    try:
        num = float(num)
        return num
    except ValueError:
        num = input("Введен не верный тип данных, введите дробное число: ")

checknum()

