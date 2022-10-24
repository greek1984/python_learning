
# Реализуйте RLE алгоритм: модуль сжатия и восстановления данных.


with open('data42.txt', 'w') as text:
    text.write(input('Введите фрагмент: \n'))
with open('data42.txt', 'r') as text:
    text = text.read()

# sent = input("Введите текст для кодировки: \n")

def coding(text):
    count = 1
    rle = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            rle = rle + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        rle = rle + str(count) + text[-1]
    return rle

def decoding(text):
    number = ''
    rle = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            rle = rle + text[i] * int(number)
            number = ''
    return rle


print(f"Текст после кодировки: {coding(text)}")
print(f"Текст после дешифровки: {decoding(coding(text))}")

