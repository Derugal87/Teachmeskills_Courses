n = int(input(''))
some_list = [int(input('')) for i in range(n)]
add_list = []
add_list_1 = []

# for i in some_list[:1]:
#     for j in some_list[1:]:
#         add_list.append(j)
#     add_list.append(i)
# print(f'Using "for" loop:   {add_list}')

for i in some_list[1:]:
    add_list.append(i)
add_list.append(some_list[0])
print(f'Using "for" loop:   {add_list}')


count = 1
while count < len(some_list):
    add_list_1.append(some_list[count])
    count += 1
    if count == len(some_list):
        add_list_1.append((some_list[0]))
print(f'Using "while" loop: {add_list_1}')
