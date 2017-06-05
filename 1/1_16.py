def inner_prod(v1, v2):
    """inner production of two vectors."""
    summ = 0
    for i in range(v1):
        summ += v1[i] * v2[i]
    return summ


def matmult3(m, v):
    return [inner_prod(r, v) for r in m]


av = [1, 2, 3]
bv = [4, 5, 6]

print(matmult3(av, bv))
