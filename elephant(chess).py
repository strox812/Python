x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())

if x_2 == (x_1 + 1) and y_2 == (y_1 + 1) or x_2 == (x_1 - 1) and y_2 == (y_1 - 1):
    print('YES')
elif x_2 == (x_1 + 1) and y_2 == (y_1 - 1) or x_2 == (x_1 - 1) and y_2 == (y_1 + 1):
    print('YES')
    
elif x_2 == (x_1 + 2) and y_2 == (y_1 + 2) or x_2 == (x_1 - 2) and y_2 == (y_1 - 2):
    print('YES')
elif x_2 == (x_1 + 2) and y_2 == (y_1 - 2) or x_2 == (x_1 - 2) and y_2 == (y_1 + 2):
    print('YES')
    
elif x_2 == (x_1 + 7) and y_2 == (y_1 + 7) or x_2 == (x_1 - 7) and y_2 == (y_1 - 7):
    print('YES')
elif x_2 == (x_1 + 7) and y_2 == (y_1 - 7) or x_2 == (x_1 - 7) and y_2 == (y_1 + 7):
    print('YES')
else:
    print('NO')
