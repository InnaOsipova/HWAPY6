#ЗАДАЧА 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random as r

# some_list=[r.randint(2, 10) for _ in range(int(input("Введите количество символов в списке :")))]
# print(some_list)
# summa = sum([some_list[i] for i in filter(lambda i: not i%2 ==0, range(len(some_list)))])
# print(summa)
# Пример 
# [7, 3, 2, 6, 4, 7]
# 16


#ЗАДАЧА 2
# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55  

# print(round(sum([(1+(1/i))**i for i in range(1, int(input('введите количество чисел последовательности : '))+1)]), 3))

#пример
# введите количество чисел последовательности : 5
# 11.55



# ЗАДАЧА 3
#  натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# # Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print({x: x*3+1 for x in range(1, int(input('Введите число n: '))+1)})



