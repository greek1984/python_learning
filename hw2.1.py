

# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
#    - 6782 -> 23
#    - 0,56 -> 11

numberA = input('Введите вещественное число: ')
print(type(numberA))
sum = 0
for i in numberA:
    if i != '.':
        sum += int(i)
print(sum)

