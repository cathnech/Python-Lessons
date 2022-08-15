# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os


text = open('text.txt', 'r').read()
print(f'Начальный текст: {text}')

def encode(string):
    count = 1
    result = []
    for x, item in enumerate(string):
        if x == 0:
            continue
        elif item == string[x - 1]:
            count += 1
        else:
            result.append((string[x - 1], count))
            count = 1
    result.append((string[len(string) - 1], count))
    return result
def formatOutput(string):
    result = []
    for item in string:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(string(item[1]) + item[0])
    return ''.join(result)
def decode(string):
    result = []
    for item in string:
        result.append(item[0] * item[1])
    return ''.join(result)

encoding = encode(text)

f = open('rle.txt', 'w').write(formatOutput(encoding))

print(f'RLE: {formatOutput(encoding)} \n ENCODE: {decode(encoding)}')
text.close
f.close
