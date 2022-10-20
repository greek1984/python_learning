
# 3) Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите значения последовательности через пробел: \n").split()))
print(lst)
for i in lst:
    lst.count(i)
    count = lst.count(i)
for i in lst:
    if count > 1:
        lst.remove(i)
print(lst)

















