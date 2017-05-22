def power(a, b):
    result = 1
    while b >= 0:
        result = result * a
        b -= 1
    return result

print(power(2, 9))
