def fact2(n):
    fact = 1
    if n > 0:
        if n % 2:
            for i in range(1, n + 1, 2):
                fact *= i
        else:
            for i in range(2, n + 1, 2):
                fact *= i
        print(fact)


def main(k):
    for i in k:
        fact2(i)


main([1, 2, 3, 4, 5])
