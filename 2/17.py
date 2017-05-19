import random


def matrixmult(m1, m2):
    s = 0  # сумма
    t = []  # временная матрица
    m3 = []  # конечная матрица
    if len(m2) != len(m1[0]):
        print("Error")

    else:
        r1 = len(m1)  # количество строк в первой матрице
        c1 = len(m1[0])  # Количество столбцов в 1
        r2 = c1  # и строк во 2ой матрице
        c2 = len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + m1[z][i] * m2[i][j]
                t.append(s)
                s = 0
            m3.append(t)
            t = []
    return m3

# testing for random values

def creatematrix(r, c):
    t = []
    m = []
    for i in range(0, r):
        for j in range(0, c):
            t.append(random.randint(1, 10))
        m.append(t)
        t = []
    return m


c1 = 1
r2 = 2
while c1 != r2:
    print("Кол-во столбцов в первой матрице должно быть = кол-ву строк 2 матрицы")
    r1 = int(input())
    c1 = int(input())
    r2 = int(input())
    c2 = int(input())

m1 = creatematrix(r1, c1)
m2 = creatematrix(r2, c2)

print(m1)
print(m2)

m3 = matrixmult(m1, m2)
print(m3)