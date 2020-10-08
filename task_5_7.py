def prepare_data():
    size = input('Enter size of matrix: ').split(' ')
    size = [int(i) for i in size]
    if size[0] != size[1]:
        print('Print square matrix')
        exit(0)

    print('Enter matrix: ')
    mx = [input('').split(' ') for _ in range(size[0])]
    mx = [[int(i) for i in row] for row in mx]
    operation(mx, size)


def operation(mx, size):
    main = [mx[i][i] for i in range(0, size[0])]
    maxi = []
    index = []

    for y, row in enumerate(mx):
        for x, value in enumerate(row):
            if value == max(row):
                maxi.append(value)
                index.append(x)

    for i in range(len(main)):
        if main[i] < maxi[i]:
            mx[i][i] = maxi[i]
            mx[i][index[i]] = main[i]

    print('New matrix: ')
    for i in mx:
        print(i)


if __name__ == '__main__':
    prepare_data()
