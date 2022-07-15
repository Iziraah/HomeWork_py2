#Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите количество элементов: '))
list = []
for i in range(-n, n+1):
   list.append(i)
print(list)

random.shuffle(list)
print(list)
