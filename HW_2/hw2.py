# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

print('\ntask1:\nПрограмма, которая принимает на вход вещественное число и показывает сумму его цифр.')
from curses.ascii import isdigit
from distutils.command.sdist import sdist

num = input()
res = 0
for i in num:
    if i.isdigit():
        res += int(i)
print(res)



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print('\ntask2:\nnПрограмма, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
#факториал типа?
import math                                #способ 1
def factorial_funk(n: int) -> int:         #способ 2
    if n == 0:
        return 1
    f = n*factorial_funk(n-1)
    print(f, end=' ')
    return f

n = int(input())
# print('[', end=' ')
# for i in range(1,n+1):
#     print(math.factorial(i), end=' ')    #способ 1
# print(']')
factorial_funk(n)                          #способ 2


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
print('\ntask3:Список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')

def funk3(n):
    sum = 0
    listik = {i:((1+1/i)**i) for i in range(1,n+1)}
    for i in listik:
        sum += listik.get(i)
    print('sum =',sum)
    return {i:((1+1/i)**i) for i in range(1,n+1)}
n = int(input())
print(funk3(n))




# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

print('\ntask4:\nЗадайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')
import random

def funk4(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-n, n))
    return arr

def sum_arr(m,arr):
    s = 0
    split_m = m.split(',')
    for i in split_m:
        s +=arr[int(i)-1]
    return s

n = int(input())
array = funk4(n)
print(array)
m = input("Enter positions in array to sum they:(separate by ',')")
print(sum_arr(m,array))



# Реализуйте алгоритм перемешивания списка.
print('\ntask5:\nАлгоритм перемешивания списка.')

def mix_arr(arr):
    for i in range(len(arr)-1, -1, -1):
        j = random.randint(0, len(arr)-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = input("Enter a arr(separate by ','): ")
split_arr = [int(i) for i in arr.split(',')]
print(split_arr)
print(mix_arr(split_arr))