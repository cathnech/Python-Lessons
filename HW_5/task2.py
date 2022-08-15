# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
candies   =   221
max_candy = 28

def print_text():
    print(f'Количество конфет сейчас: {candies}')
def human_turn():
    global candies
    candy_count = int(input('Введите количество конфет:')) 
    if isCountValid(candy_count):
        candies = candies - candy_count
    else:
        print(f'Количество конфет может быть только от 0 до {max_candy}, и не больше {candies}')
        human_turn()
def ai_turn():
    global candies
    if ((candies - max_candy) > max_candy):
        x = random.randint(1, max_candy)
    elif((candies - max_candy) <= max_candy):
        x = candies-(max_candy+1)
    else:
        x = candies
    candies -= x
    print(f'Компьютер походил: {x}')
def isCountValid(x):
    return (0 < x <= max_candy) and (x <= candies) 
def isWinner():
    return True if (candies <= 0) else False

while True:    
    print_text()
    human_turn()
    if isWinner():
        print('Победил человек')
        break
    print_text()
    ai_turn()
    if (isWinner()):
        print('Победил ИИ')
        break
print('Игра закончена')