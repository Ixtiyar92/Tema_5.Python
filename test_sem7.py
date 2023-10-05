# num_list = [2, 4, 4, 8]

# через map:
# def mult2(x):
#     return x*2

# result = list(map(mult2, num_list))
# res_1 = [mult2(i) for i in num_list]
# print(result, " | ", res_1)

# через lambda:
# result = list(map(lambda x: x*2, num_list))
# print(result)


num_list = [2, 4, 4, 8, 1, 3, 5]
# из списка выбрать четные числа и вернуть кортеж из этого числа и его в квадрате
squares = list(map(lambda y: (y, y**2), filter(lambda x: x%2 == 0, num_list)))
print(squares)