guests = abs(int(input('Введите количество гостей: ')))
if guests > 50:
    print('ресторан')
elif guests < 20:
    print('дом')
else:
    print('кафе')