count = input()
count = int(count)
i = 0
allTrue = True

while i < count:
    numb = int(input())
    if numb != 1:
        allTrue = False
    i += 1

print(allTrue)
