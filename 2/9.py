B = 0
A = 1
m = int(input())
for k in range(1, m + 1):
    A = 1
    for i in range(1, k + 1):
        A = i * A
    B = B + A
print(B)
