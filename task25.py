# Задача 25:  Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n. Порядок символов исходной строки не меняется.

# Пример:
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# Решение через словари
string = input('Введите строку: ').split()
d = dict() # Создаем словарь, куда будем сохранять символы из строки как ключи, а количество вхождений как значения
for i in string:
    if i in d:
        print(f"{i}_{d[i]}", end=' ') # Если символ есть в словаре распечатываем его и количество вхождений
    else:
        print(i, end=' ') # Если нет - распечатываем один символ
    d[i] = d.get(i, 0) + 1 # Создаем ключ и присваиваем ему значение 1. Если же такой ключ есть, то увеличиваем значение на 1


# Решение через срезы
# sequence = 'a a a b a c b b d'.split()
# result = ''
# for i in range(len(sequence)):
#     if sequence[0:i:].count(sequence[i]) == 0:
#         result += sequence[i]
#     else:
#         result += f'{sequence[i]}_{sequence[0:i].count(sequence[i])}'
#     print(sequence[0:i], result)
# print(result)

# Решение через list comprehenshion и срезы
# sequence = 'a a a b a c b b d'.split()
# result = ''
# print(sequence)
# result = [(sequence[i] if sequence[0:i:].count(sequence[i]) == 0 else
#             f'{sequence[i]}_{sequence[0:i:].count(sequence[i])}') for i in range(len(sequence))]
# print(' '.join(result))