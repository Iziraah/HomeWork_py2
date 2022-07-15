# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
numbers = []
numbers_sum = []
sum = 0
for i in range(1, n+1):
    i = (1+1/i)**i
    numbers.append(i)
    sum += i
    numbers_sum.append(sum)
   # print(sum)
print(numbers)
print(numbers_sum)
