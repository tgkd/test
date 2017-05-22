# Написать функцию sigma с двумя аргументами – числом n и функцией f(x). Функция sigma вычисляет f(1)+f(2)+f(3)+…+f(n).


def sigma(n, func):
    summ = 0
    for i in range(1, n):
        func_res = func(i)
        summ += func_res
    return summ


def calc_func(numb):
    return numb

result = sigma(4, calc_func)

print(result)
