import math


def sin1(x, eps):
    if eps <= 0:
        print("Epsilon is bigger than 0")

    n = x
    s = x
    i = 3
    while abs(n) > eps:
        n *= (-1) * x * x / ((i - 1) * i)
        i += 2
        s += n
    return s


eps = 0.01
for i in range(0, 6):
    x = math.pi / 4
    print(f'eps = {eps}; sin({x}) = {sin1(x, eps)} and {math.sin(x)}')
    eps /= 10
