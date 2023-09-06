# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Пример:
# Ввод: 5 6 -> Вывод: 2 3

# 1 способ:
s = int(input("Сумма чисел: "))
p = int(input("Произведение чисел: "))
for x in range(s):
    for y in range(p):
        if x + y == s and x * y == p:
            print(x, y)


# 2 способ: через теорему Виетта
# ax2 + bx + c;    D = b2 - 4ac;     x = (-b +- корень из D) / 2a
# S = b, P = c;    D = S2 - 4P;      x = (-S +- корень из S2 - 4P) / 2
# s = int(input("Сумма чисел: "))
# p = int(input("Произведение чисел: "))
# x = (-s + (s**2 - 4*p)**(0.5)) / 2
# y = (-s - (s**2 - 4*p)**(0.5)) / 2
# print(x, y)