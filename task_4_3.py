some_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
some_dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

new_list = list(some_dict)

for i in new_list:
    new_key = i + str(len(i))
    some_dict[new_key] = some_dict.pop(i)
print(f'Using "for" loop:   {some_dict}')

i = 0
while i < len(new_list):
    new_key_1 = new_list[i] + str(len(new_list[i]))
    some_dict_1[new_key_1] = some_dict_1.pop(new_list[i])
    i += 1
print(f'Using "while" loop: {some_dict}')

exit(0)