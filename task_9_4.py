def operation(func):
    def wrapper(*args, **kwargs):
        lst = []
        for i, value in kwargs.items():
            lst.append(f'{i}={value}')
        return func(args[::-1] + tuple(lst))

    return wrapper


@operation
def start(*args, **kwargs):
    for i in args:
        print(*i, sep=', ', end=' ')


start(1, 2, 3, 4, a=1, b=2)
