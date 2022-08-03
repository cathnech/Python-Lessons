# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print('\ntask1:\nЗадайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')

def funk_sum(arr):
    sum = 0
    for i in range(1,len(arr),2):
        sum+=arr[i]
    return sum
arr = input("Enter a arr(separate by ','): ")
split_arr = [int(i) for i in arr.split(',')]
print(split_arr)
print(funk_sum(split_arr))

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
print('\ntask2:\nНапишите программу, которая найдёт произведение пар чисел списка. ')

def funk_arr2sum(arr):
    print(arr)
    sum = []
    b = len(arr)//2+1 if len(arr)%2 > 0  else len(arr)//2
    for i in range(b):
        sum.append(arr[i]*arr[-i-1])
    return sum

arr = input("Enter a arr(separate by ','): ")
split_arr = [int(i) for i in arr.split(',')]
print('answer',funk_arr2sum(split_arr))
print('test',funk_arr2sum([2, 3, 4, 5, 6]))
print('test2',funk_arr2sum([2, 3, 5, 6]))


# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print('\ntask3:\nЗадайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.')

def func_minVSmax(arr):
    print(arr)
    res = [arr[0] % 1,arr[0] % 1,0] # res[min,max,buffer]
    for i in range(len(arr)):
        res[2] = round(arr[i] % 1, 2)
        if res[2] < res[0] and res[2] != 0:
            res[0] = res[2]
        elif res[2] > res[1]:
            res[1] = res[2]
    return round(res[1]-res[0],2)

test = [1.1, 1.2, 3.1, 5, 10.01]
print('min - max(test):',func_minVSmax(test))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
print('\ntask4:\nНапишите программу, которая будет преобразовывать десятичное число в двоичное.')

def funk_in01(n):
    num = ''
    while n > 0:
        num = str(n % 2) + num
        n//=2
    return num

n = int(input())
print(funk_in01(n))


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
print('\ntask5:\nЗадайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')

def funk_febonachi(n):
    ans_arr = [0]
    j = 1
    for i in range(1,n+1):
        if i%2 == 0:
            ans_arr.insert(0,-j)
        else:
            ans_arr.insert(0,j)
        ans_arr.append(j)
        j += ans_arr[-2]
    return ans_arr

n = int(input())
print(funk_febonachi(n))
