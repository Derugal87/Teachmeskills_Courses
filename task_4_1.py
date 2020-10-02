n = int(input(''))
some_list = [int(input('')) for i in range(n)]

new_list = []
new_list_1 = []

for i in some_list:
    i *= -2
    new_list.append(i)
print(f'Using "for" loop:   {new_list}')

i = 0
while i < len(some_list):
    elem = some_list[i] * (-2)
    new_list_1.append(elem)
    i += 1
print(f'Using "while" loop: {new_list_1}')
