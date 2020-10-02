n = int(input(''))
some_list = [int(input('')) for i in range(n)]

count = 0
for i in some_list:
    if not i % 2:
        count += 1
print(f'Using "for" loop - number of even numbers = {count}.')

count_1 = 0
n = 0
while n < len(some_list):
    if not some_list[n] % 2:
        count_1 += 1
    n += 1
print(f'Using "while" loop - number of even numbers = {count_1}.')
