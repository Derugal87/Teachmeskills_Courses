import random
import copy


def printer(matrix):
    for row in matrix:
        print(row)


# 1 task
print('task 1')
n, m = map(int, input('Enter size of matrix: ').split(' '))

print('Processing matrix: ')
mx = [[random.randrange(0, 20) for y in range(m)] for x in range(n)]

printer(mx)

# 2 task
print('\ntask 2')
print(f'MAX element is: {max(max(mx[i]) for i in range(n))}')

# 3 task
print('\ntask 3')
print(f'MIN element is: {min(min(mx[i]) for i in range(n))}')

# 4 task
print('\ntask 4')
print(f'SUM of elements is: {sum(sum(mx[i]) for i in range(n))}')

# 5 task
print('\ntask 5')
maxi_5 = max(map(sum, mx))
for i, value in enumerate(mx):
    if sum(value) == maxi_5:
        print(f'MAX row index is: {i}')

# 6 task
print('\ntask 6')
maxi_6 = max(map(sum, [*zip(*mx)]))
for i, value in enumerate([*zip(*mx)]):
    if sum(value) == maxi_6:
        print(f'MAX column index is: {i}')

# 7 task
print('\ntask 7')
mini_7 = min(map(sum, mx))
for i, value in enumerate(mx):
    if sum(value) == mini_7:
        print(f'MIN row index is: {i}')

# 8 task
print('\ntask 8')
mini_8 = min(map(sum, [*zip(*mx)]))
for i, value in enumerate([*zip(*mx)]):
    if sum(value) == mini_8:
        print(f'MIN column index is: {i}')

# 9 task
print('\ntask 9')
mx_9 = copy.deepcopy(mx)
for i in range(m):
    for j in range(n):
        if i < j:
            mx_9[i][j] = 0
print('0 indexes above main diagonal:')
printer(mx_9)
# 10 task
print('\ntask 10')
for i in range(n):
    for j in range(m):
        if i > j:
            mx[i][j] = 0
print('0 indexes under main diagonal:')
printer(mx)
