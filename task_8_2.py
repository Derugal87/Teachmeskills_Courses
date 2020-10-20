def polyndrom(lst):
    for i in lst:
        if i == i[::-1]:
            print(i)


polyndrom([input() for x in range(3)])
