# СПИСКИ
# list_1 = [] # создание пустого списка
# list_1 = list() # создание пустого списка
# list_1 = [1, 2, 3, 8]

# print(len(list_1)) # узнать количество элементов в списке
# print(list_1[0]) # вывести первый (любой другой) элемент списка
# print(list_1[-1]) # вывести последний (любой другой) элемент списка

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # добавление в конец нашего списка элемента
# print(list_1)

# list_1 = []
# for i in range(5): 
#     list_1.append(i)
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0 (удаление с конца элемента из нашего списка)
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# list_1 = [12, 7, -1, 21, 0]
# list_1.insert(2, 11) # добавление элемента (числа 11 на место индекса 2) в список
# print(list_1) # [12, 7, 11, -1, 21, 0] 

# СРЕЗЫ СПИСКОВ
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# КОРТЕЖИ
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(t) # red green blue

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue

# СЛОВАРИ
# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# print(dictionary)

# МНОЖЕСТВА
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# ОПЕРАЦИИ СО МНОЖЕСТВАМИ
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}   копирование множества "a" в множество "c"
# print(c)
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}   объединение множеств "a" и "b"
# print(u)
# i = a.intersection(b) # i = {8, 2, 5}     пересечение множеств "a" и "b"
# print(i)
# d1 = a.difference(b) # dl = {1, 3}        разность множеств: из "a" вычитаем "b"
# print(d1)
# d2 = b.difference(a) # dr = {13, 21}      разность множеств: из "b" вычитаем "a"
# print(d2)
# q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}    сначала в скобках пересечение множеств выполняем, потом объединяем "a" и "b", в конце выполняем разность
# print(q)

# НЕИЗМЕНЯЕМОЕ ИЛИ ЗАМОРОЖЕННОЕ МНОЖЕСТВО:
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


# LIST COMPREHENSION (генератор списка):
# Задача 1.Создать список, состоящий из четных чисел в диапазоне от 1 до 100.

# list_1 = []              # создаём пустой список
# for i in range(1, 101):  # пока i в диапазоне от 1 до 100
#     list_1.append(i)     # добавляем i при каждой итерации списка
# print(list_1)            # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1)

# Задача 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# print(list_1)

# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# print(list_1)

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]
