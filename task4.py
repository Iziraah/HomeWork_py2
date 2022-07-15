#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. 
#Позиции вводит пользователь через пробел

n = int(input('Введите число: '))
list = []
for i in range(-n, n+1):
   list.append(i)
print(list)

a, b = (int(i) for i in input('Введите позиции элементов через пробел: ').split())
multiplication = list[a]*list[b]
print(multiplication)
