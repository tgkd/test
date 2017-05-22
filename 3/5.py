def solve(mat, mul):
    width = len(mat)
    if width == 1:
        return mul * mat[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(mat[j][k])
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * mat[0][i])
        return total


matrix = [[6, -4, 3], [2, -3, -4], [1, 4, -3]]
print(solve(matrix, 1))
