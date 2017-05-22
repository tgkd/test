arr = [int(x) for x in input().split()]

res = []
for i in arr:
    if i not in res:
        res.append(i)

print(res)
