is_first = True
numb = 0
mult = 1
count = 0
while (numb > 0 or is_first):
    numb = input()
    if numb > 0:
        mult = numb * mult
        count += 1
    is_first = False

print(mult)