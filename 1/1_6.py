n = input()
i = 1
result = 1
multi = 1

while i <= n:
    print(i)
    multi = multi * i+1 + i+2
    result = multi + result
    i += 1

print(multi)
print(result)