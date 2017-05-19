count = int(input())
i = 0
elements = []
while i < count:
    numb = int(input())
    elements.append(numb)
    i += 1

prev = None
some_eq = False
all_uniq = False
all_same = False

for el in range(count-1):
    for el2 in range(el+1, count):
        if elements[el] == elements[el2]:
            some_eq = True

print('all unique')

