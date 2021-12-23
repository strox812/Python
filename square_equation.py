from math import pow
a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - (4 * a * c)

if d < 0:
    print('Нет корней')
elif d == 0:
    x = - (b) / (2 * a)
    print(x)
elif d > 0:
    x_1 = (-(b) + pow(d, 2)) / (2 * a)
    x_2 = (-(b) - pow(d, 2)) / (2 * a)
    print(min(x_1, x_2), max(x_1, x_2), sep='\n')
