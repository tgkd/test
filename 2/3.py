#3. Вводится массив n-чисел, затем вводится число k. Из массива удалить все вхождения числа k.

s = input()
numbers = list(map(int, s.split(' ')))

k = int(input())
buf = []

for n in numbers:
    if n != k:
        buf.append(n)


print(buf)
