color_1, color_2 = input(), input()
if color_1 == 'красный' and color_2 == 'синий' or color_2 == 'красный' and color_1 == 'синий':
    print('фиолетовый')
elif color_1 == 'желтый' and color_2 == 'красный' or color_2 == 'желтый' and color_1 == 'красный':
    print('оранжевый')
elif color_1 == 'желтый' and color_2 == 'синий' or color_2 == 'желтый' and color_1 == 'синий':
    print('зеленый')
elif color_1 == 'красный' and color_2 == 'красный' or color_2 == 'красный' and color_1 == 'красный':
    print('красный')
elif color_1 == 'синий' and color_2 == 'синий' or color_2 == 'синий' and color_1 == 'синий':
    print('синий')
elif color_1 == 'желтый' and color_2 == 'желтый' or color_2 == 'желтый' and color_1 == 'желтый':
    print('желтый')
elif color_1 != 'красный' or color_1 != 'синий' or color_1 != 'желтый' or color_2 != 'красный' or color_2 != 'синий' or color_2 != 'желтый':
        print('ошибка цвета')
