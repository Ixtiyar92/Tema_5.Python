# with open('base.txt', 'a', encoding='utf-8') as file:
#     file.write('Привет, мир!\n')

with open('base.txt', 'r', encoding='utf-8') as file:
    apples = file.read()
print(apples)
num = int(apples.split()[0])
print(num + 10)
with open('base.txt', 'a', encoding='utf-8') as file:
    file.write(f' + {apples} = {num + 10} яблок')