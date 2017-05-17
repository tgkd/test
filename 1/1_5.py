n = input()
i = 0
result = 0

while i <= n:
    if (i % 2) == 0:
        result -= i
    else:
        result += i 
    i += 1
print(result)