num_1, num_2, sign = int(input()), int(input()), input()
if sign == '/':
    if num_2 == 0:
        print('На ноль делить нельзя!')
    elif num_1 != 0 or num_2 != 0:
        print(num_1 / num_2)
elif sign == '*':
    print(num_1 * num_2)
elif sign == '+':
    print(num_1 + num_2)
elif sign == '-':
    print(num_1 - num_2)
else:
    print('Неверная операция')
