count = 13

some_list = []
previous = 1
current = 1
some_list.extend([previous, current])
for n in range(count):
    temporary = previous + current
    previous = current
    current = temporary
    some_list.append(current)
print(f'Using "for" loop:   {some_list}, в списке {len(some_list)} элементов.')

some_list_1 = []
previous_1 = 1
current_1 = 1
some_list_1.extend([previous_1, current_1])
i = 0
while i < count:
    temporary_1 = previous_1 + current_1
    previous_1 = current_1
    current_1 = temporary_1
    some_list_1.append(current_1)
    i += 1
print(f'Using "while" loop: {some_list_1}, в списке {len(some_list_1)} элементов.')
