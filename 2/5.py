# Вводится количество мест и количество абитуриентов, затем баллы абитуриентов в порядке убывания.
# Вывести количество абитуриентов с полупроходным баллом. Массивы не использовать.

pl_count = int(input())
std_count = int(input())
i = 0
prev = None
res_count = 0
no_place = False

while i < std_count:
    new_std = int(input())

    if pl_count != 1:
        prev = new_std
        pl_count -= 1
    else:
        if prev == new_std or no_place or res_count == 0:
            res_count += 1
            prev = new_std
        else:
            no_place = True
            break

print(res_count)

