# Создайте программу для игры в ""Крестики-нолики"".

import random

dot_empty = '.'
dot_o = 'O'
dot_x = 'X'
size   =   3
winCount = 3 # кол-во фишек

# size   =   5
# winCount = 4 # кол-во фишек

# size   =   int(input('Введите размер поля'))
# winCount = int(input('Введити победное значение фишек')) # кол-во фишек

table_game = [[dot_empty] * size for i in range(size)]

def print_table(table):
    for i in range(0,len(table)):
        print(table[i])
def human_turn():
    x,y = -1, -1
    x += int(input('Введите координату X')) 
    y += int(input('Введите координату Y')) 
    if isCellValid(x,y):
        table_game[y][x] = dot_x
    else:
        print('Поле занято, измените свой выбор')
        human_turn()
def ai_turn():
    x = 0
    y = 0
    flag = 0
    for i in range(size):
        for j in range(size):
            if (checkWinPosition(j,i)):
                flag = 1
                x=j
                y=i
                break
        if (flag == 1): break
    if (flag != 1):
        while not (isCellValid(x, y)):
            x   =   random.randint(0, size-1)
            y   =   random.randint(0, size-1)
        table_game[y][x] = dot_o
    print(f'Компьютер походил: {(x+1)} и {(y+1)}')
def isCellValid(x,y):
    return ((size > x >= 0) and (size > y >= 0)) and (table_game[y][x] == dot_empty)
def isWinner(symb):
    flag1,flag2,flag3,flag4 = 0,0,0,0
    for i in range(size):
        flag1 = 0
        flag2 = 0
        flag3 = (flag3+1) if (table_game[i][i] == symb) else 0
        flag4 = (flag4+1) if (table_game[i][size - 1 - i] == symb) else 0
        if (flag3 == winCount or flag4 == winCount): return True
        for j in range(size):
            flag1 = (flag1+1) if (table_game[i][j] == symb) else 0
            flag2 = (flag2+1) if (table_game[j][i] == symb) else 0
            if (flag1 == winCount or flag2 == winCount): return True
    return False
def isMapFull():
    for i in range(size):
        if (table_game[i].count(dot_empty)): return False
    return True
def checkWinPosition(x, y):
    if (table_game[y][x] != dot_empty): return False
    table_game[y][x] = dot_o
    if (isWinner(dot_o)): return True
    table_game[y][x] = dot_x
    if (isWinner(dot_x)):
        table_game[y][x] = dot_o
        return True
    table_game[y][x] = dot_empty
    return False

print_table(table_game)
while True:    
    human_turn()
    print_table(table_game)
    if isWinner(dot_x):
        print('Победил человек')
        break
    elif (isMapFull()):
        print('Ничья')
        break
    ai_turn()
    print_table(table_game)
    if (isWinner(dot_o)):
        print('Победил ИИ')
        break
    elif (isMapFull()):
        print('Ничья')
        break
print('Игра закончена')