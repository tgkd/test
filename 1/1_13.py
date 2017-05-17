#wtf?

count = int(input())
min_val = 1
max_val = 100
i = 0

oneTrue = False

while i < count:
    numb = int(input())
    if numb < min_val:
        min_val = numb
    if numb > max_val:
        max_val = numb
    i += 1

print(oneTrue)
