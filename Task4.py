# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter= int(input('Input a quarter number : '))
if quarter ==1:
    print(f'The range of possible coordinates of points in  quarter {quarter} is x > 0 and y > 0')
elif quarter ==2:
    print(f'The range of possible coordinates of points in  quarter {quarter} is x < 0 and y > 0')
elif quarter ==3:
    print(f'The range of possible coordinates of points in  quarter {quarter} is  x < 0 and y < 0')
elif quarter ==4:
    print(f'The range of possible coordinates of points in  quarter {quarter} is x > 0 and y < 0')
else:
    print('Non-existent quarter value')