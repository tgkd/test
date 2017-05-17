numb = 0
summ = 0
z_count = 0

while z_count < 3:
    numb = input()
    numb = int(numb)
    if numb == 0:
        z_count += 1
    summ += numb

print(summ)
