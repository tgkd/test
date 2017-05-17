start = input()
start = int(start)
step = input()
step = int(step)
count = input()
count = int(count)
summ = 0
i = 0
is_first = True
prev = 0

while i <= count:
    if is_first:
        summ += start
        prev = start
        is_first = False
    else:
        prev = prev * step
        summ += prev
    i += 1

print(summ)

