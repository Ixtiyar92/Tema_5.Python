# Дополнительная Задача: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают
# число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения
# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36

# Способ 1:
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])


# print_operation_table(lambda x, y: x * y)

# Способ 2:
def show_table(table: list[list[int]]) -> None:
    ''' Просто красиво печатает матрицу.'''
    print('\n'.join('\t'.join(map(str, row)) for row in table))

def print_operation_table(oper: callable, num_rows: int = 6, num_columns: int = 6) -> None:
    '''
    Выводит таблицу для чисел с заданной операцией oper,
    числом столбцов num_columns и строк num_rows
    '''
    table = [list(range(i, i+num_columns)) for i in range(1, num_rows+1)]
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            table[i][j] = oper(table[i][0], table[0][j])
    show_table(table)

n = 6
m = 6
print_operation_table(lambda x, y: x * y, n, m)