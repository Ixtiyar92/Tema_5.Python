# Задача 27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input:
# She\n sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells
# Output: 13

string = input('Введите строку: ').split()
new_set = set()
for word in string:
    new_set.add(word.lower().strip(".,\\n"))
print(len(new_set))