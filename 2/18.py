def magic_square(matrix):
    i_size = len(matrix[0])
    sum_list = []

    for col in range(i_size):
        sum_list.append(sum(row[col] for row in matrix))

    sum_list.extend([sum(lines) for lines in matrix])

    dl_result = 0
    for i in range(0, i_size):
        dl_result += matrix[i][i]
    sum_list.append(dl_result)

    dr_result = 0
    for i in range(i_size - 1, -1, -1):
        dr_result += matrix[i][i]
    sum_list.append(dr_result)

    if len(set(sum_list)) > 1:
        return False
    return True

print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print(magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
