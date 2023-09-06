# Задача 21: Напишите программу для печати всех уникальных значений в словаре.
# [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

dict = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, {"VI" : "S005"}, {"VII" : "S005"}, {"V" : "S009"}, {"VIII" : "S007"}]

# Способ 1: стандартный
new_set = set()
for i in dict:
    for k in i.values():
        new_set.add(k)
print(new_set)

# Способ 2: через List Comprehension
# print(set((list(k.values())[0]) for k in dict))