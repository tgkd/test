is_first = True
numb = 0
summ = 0
count = 0
while numb > 0 or is_first:
    numb = input()
    if numb > 0:
        summ += numb
        count += 1
    is_first = False


print(summ/count)