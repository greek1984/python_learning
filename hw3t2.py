# 2) Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

first_list = list(map(int, input("Введите числа через пробел:\n").split()))
second_list = []
for i in range((len(first_list)+1)//2):
    second_list.append(first_list[i]*first_list[len(first_list)-1-i])
print(second_list)