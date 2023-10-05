# def f(x):
#     return x*x
# a = f
# print(f(5))
# print(f(5))



# def calk1(a, b):
#     return a+b
# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))
# math(calk2, 5, 45)



# def calk2(a, b):
#     return a*b
# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)



# Задача 1: В списке хранятся числа.
# Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# 1: написали простую функцию, где выводится бычный цикл
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# 2: преобразовали эту функцию в виде отдельных функций
# def select(f, col):     # по сути то же самое что и функция map
#     return [f(x) for x in col]
# def where(f, col):      # по сути то же самое что и функция filter
#     return [x for x in col if f(x)]

# 3: изучили функцию map и добавили в нашу программу
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

# data = "15 156 96 3 5 8 52 5"
# print(data)

# # data = data.split()
# # print(data)
# data = list(map(int, data.split()))
# print(data)

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# 4: изучили функцию filter и добавили в нашу программу
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# функция zip:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

# функция enumerate:
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)


# режим файла a:
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# Ещё один способ записи данных в файл:
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# режим файла r:
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


# Модуль os:

# 1) os.chdir(path) - смена текущей директории
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')

# 2) os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'


# os.path - является вложенным модулем в модуль os и реализует некоторые
# полезные функции для работы с путями, такие как:

# 3) os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) # 'main.py'

# 4) os.path.abspath(path) - возвращает нормализованный абсолютный путь
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'


# Модуль shutil: import shutil

# Познакомимся с базовыми функциями данного модуля:
# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в
# файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
# должен указывать на директорию, а не на символическую ссылку.
