# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
print('\ntask1:\nВычислить число c заданной точностью d')

import math

def funk_pi(d):
    p = 0
    for i in range(d):
        s = 8*i+1
        p += 1/(16**i)*(4/(s)-2/(s+3)-1/(s+4)-1/(s+5))   
    return p

d = (input().replace(',', '.')).split('.')
d = len(d[1])

print(round(math.pi,d))
print(round(funk_pi(d),d))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
print('\ntask2:\nЗадайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.')

def funk_naturaln(n):
   i = 2
   res = []
   while i * i <= n:
       while n % i == 0:
           res.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       res.append(n)
   return res

n = int(input())
print(funk_naturaln(n))


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.
print('\ntask3:\nЗадайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.')

def funk_without_repeat_element(arr):
    print(arr)
    res = []
    for i in range(len(arr)):
        print(arr[i],i,arr[0:i-1],arr[i+1:])
        if not((arr[i] in arr[0:i]) or (arr[i] in arr[i+1:])):
            res.append(arr[i])
    return res

arr = input("Enter a arr(separate by ','): ")
split_arr = [int(i) for i in arr.split(',')]
print(funk_without_repeat_element(split_arr))


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
print('\ntask4:\nЗадана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.')
import random

def funk_chlen(k):
    r = random.randint(0, 100)
    ch = ''
    if k > 0:
        if r > 0: f.write(f'{r} * x^{k} + ')
        return funk_chlen(k-1)
    if r > 0: ch = str(r)
    return ch+' = 0'


k = int(input())
f = open('task5.txt', 'w')
f.write(funk_chlen(k))
f.close



# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий 
# сумму многочленов.
print('\ntask5:Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий.')

def sum_chlens(n,m):
    resstr = ''
    for i in range(len(n)+len(m),-1,-1):
        buff = 0
        x = 'x^'+str(i)
        n1 = n.get(x,['','0'])
        m1 = m.get(x,['','0'])

        sign = -1 if (n1[0] == '-') != (m1[0] == '-') else 1
        buff += (int(n1[1]) + int(m1[1]))* sign
        
        if (buff > 0) and (i > 0):
            f.write(f'{buff} * {x} + ')
        elif (buff > 0) and (i == 0): 
            f.write(f'{buff} = 0')
        
def get_dict(a):
    
    a1 = a[2:-1:4]
    a2 = a[0:-1:4]
    a3 = a[3:-1:4]
    a1.append('x^0')
    a3.insert(0,'+')
 
    return dict(zip(a1,list(zip(a3,a2))))


str1 = open('first.txt', 'r').readline().split(' ')
str2 = open('second.txt', 'r').readline().split(' ')

n = get_dict(str1)
m = get_dict(str2)

f = open('result.txt', 'w')
sum_chlens(n,m)
f.close