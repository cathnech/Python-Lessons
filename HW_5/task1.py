# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# S.lower()
# S.join(список)
stroka = 'абв'
text = 'Подняты сокровища абвиспанского галеона абв «Нуэстра Сеньора деабв лас Маравильяс», затонуабввшего в 1656 году около Багамских островов'
text1 = text.split(' ')

f = lambda x: not x.count(stroka) > 0

slovo = list(filter(f,text1))
res_text = ' '.join(slovo)
print(res_text)