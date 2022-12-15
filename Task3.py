# 3.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xa=float (input('Input coordinates of point A along the axis X :'))
ya=float (input('Input coordinates of point A along the axis Y :'))
xb=float (input('Input coordinates of point B along the axis X :'))
yb=float (input('Input coordinates of point B along the axis Y :'))

import math
distans= math.sqrt((xb-xa)**2+(yb-ya)**2)
print(f'Distance between points A and B {distans}')
