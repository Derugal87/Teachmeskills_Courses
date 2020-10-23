def operation(func):
    def wrapper(lst):
        return func(lst[::2])
    return wrapper

@operation
def start(lst):
    print(lst)


start([1, 2, 3, 4, 5, 6, 0, 5, 34])