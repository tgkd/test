count = input()
count = int(count)
i = 0
oneTrue = False

while i < count:
    numb = int(input())
    if numb == 1:
        oneTrue = True
    i += 1

print(oneTrue)
