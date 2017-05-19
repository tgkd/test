input_str = str(input())
a = input_str[::-1]
if input_str == a:
    print(True)
else:
    print(False)

# hardcore mode
s_input = str(input())
x = len(s_input)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if s_input[x - i] == s_input[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
    print("no")
else:
    print("yes")
