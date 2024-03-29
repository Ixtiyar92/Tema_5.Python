# Задача 51: Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# В качестве примера характеристики можно взять проверку четности из лекции, а можно придумать свою.

# Ввод:
# 1 2 3 4 5
# lambda: x%2 == 0
# Вывод:
# False

def same_by(characteristic, objects):
    if list(filter(characteristic, objects)) == objects:
        return True
    return False

# Способ 1 через lambda:
# values = [2, 4, 6]
# print(same_by(lambda x: x%2 == 0, values))


# Способ 2 через функцию def:
def char(x):
    return x % 2 == 0

values = [2, 4, 6]
print(same_by(char, values))