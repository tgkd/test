count = int(input())
i = 0
all_eq = True
neigh_eq = False
neigh_not_eq = False

prev = None

while i < count:
    numb = int(input())
    if numb == prev:
        print()
    elif numb != prev and all_eq:
        all_eq = False
    else:
        all_eq = False
        neigh_eq = False
        neigh_not_eq = True
    prev = numb
    i += 1

print('all eq ', all_eq)
print('neigh eq ', neigh_eq)
print('neigh not eq ', neigh_not_eq)
