int_list = list(range(1, 101))
res = [0] * 101


def find_numb(input_list):
    for i in int_list:
        for j in int_list:
            if int_list[i] == input_list[j]:
                res[i] = res[i] + 1

i_list = [int(x) for x in input().split()]

find_numb(i_list)

print(res)
