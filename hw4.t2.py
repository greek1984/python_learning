N = int(input('Введите число: '))
lst = []
i = 2
for i in range(1, N):
    while i <= N:
        if N % i == 0 and i != 1:
            lst.append(i)
            N //= i
            i = 2
        else:
            i += 1
print(lst)


