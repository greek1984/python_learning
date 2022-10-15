
# 4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
number_binary = ''
while number > 0:
    umber_binary = str(number % 2) + number_binary
    number = number // 2
    print(umber_binary, end="")