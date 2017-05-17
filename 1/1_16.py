def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

av = [1, 2, 3]
bv = [4, 5, 6]

print(cross(av, bv))
