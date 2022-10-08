
# 3) Задайте список (словарь не нужно выводить!) из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = [1, 3, 5, 6]
#
# sum = 0
# for i in n:
#     i = i + 1
#     if i != 0:
#         sum += i
# print(sum)

n = int(input('Введите количество чисел в списке '))

def numbers(n):
    summ = 0
    for i in range(n):
        number = int(input(f'Введите {i + 1}е число: '))
        number = (1 + 1/number) ** number
        summ += number
        i += 1
    return summ

print('Сумма чисел равна',round((numbers(n)), 2))
