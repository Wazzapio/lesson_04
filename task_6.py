print('Начало программы.\nИтератор, генерирующий целые числа, начиная с числа 3, заканчивая числом 10.')
from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
print('Конец программы.\n')

print('Начало программы.\nИтератор, повторяющий элементы некоторого списка, определенного заранее\n'
      'до тех пор пока элементов не будет 10шт.')
from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 9:
        break
    print(el)
    с += 1
print('Конец программы.\n')
