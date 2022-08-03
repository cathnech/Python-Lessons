# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
print('\ntask1:\nНапишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным\n')
ans = 'error(number may be from 1 to 7)'
day = int(input('Enter day of week:'))
if 0<day<6:
    ans = 'no'
elif 5<day<8:
    ans = 'yes'
print(ans)


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('\ntask2:\nНапишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат\n')
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            print('for ',x,y,z,'\n',(not (x or y or z)) == (not x and not y and not z))


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('\ntask3:\nНапишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).\n')
x = int(input('Enter x(not 0):'))
y = int(input('Enter y:(not 0)'))
if x>0 and y>0:
    answer = '1'     
elif x<0 and y>0:
    answer = '2'
elif x<0 and y<0:
    answer = '3'
elif x>0 and y<0:
    answer = '4'
else:
    answer = 'error'
print(answer)

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('\ntask4:\nНапишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)\n')
num = int(input('Enter num of part coordinate plane(1,2,3,4):\n'))

if num==1:
    answer = '0 < x < +infinity and 0 < y < +infinity'     
elif num==2:
    answer = '-infinity < x <0 and 0 < y < +infinity'
elif num==3:
    answer = '-infinity < x < 0 and -infinity < y <0'
elif num==4:
    answer = '0 < x < +infinity and -infinity < y < 0'
else:
    answer = 'error'
print(answer)

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
print('\ntask5:\nНапишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.\n')
import math

xA = int(input('Enter points of A in 2D:\n'))
yA = int(input())
xB = int(input('Enter points of B in 2D:\n'))
yB = int(input())
print(round(math.sqrt(((xB - xA)**2)+((yB - yA)**2)),2))