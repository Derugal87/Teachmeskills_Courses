def operation(lst):
    m = int(lst[0])
    n = int(lst[1])
    some_list = []
    for i in range(m, n + 1):
        for k in range(2, i):
            if i % k == 0:
                some_list.append([i, k])

    for i in range(m, n + 1):
        print(f"{i}: {' '.join(map(str, [row[1] for row in some_list if row[0] == i]))}")


if __name__ == '__main__':
    operation(input('Enter numbers for m & n: ').split())
