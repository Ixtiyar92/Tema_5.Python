# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 1 3 2 1 1 6
# Output: 10

bushes = [1, 2, 3, 4, 5] # bushes - это кусты
max_berries = 0 # berries - это ягоды
count_bush = 4 # кол-во кустов

for i in range(-count_bush, len(bushes)-count_bush):
    print([bushes[i + j] for j in range(count_bush)])
    sum_berries = sum(bushes[i + j] for j in range(count_bush))
    if sum_berries > max_berries:
        max_berries = sum_berries
print(max_berries)
