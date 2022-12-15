# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day=int(input('Input the number indicating the day of the week : '))
if day in range(1,6):
    print('This day is not a weekend')
elif  day in range(6,8):   
    print('The day is a weekend')
else:
    print('Non-existent day of the week') 