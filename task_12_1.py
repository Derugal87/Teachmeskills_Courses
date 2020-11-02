class Time:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Time):
            self.__init_with_instance(*args)
        elif len(args) == 1 and type(args[0]) is str:
            self.h, self.m, self.s = map(int, args[0].split(':'))
            seconds = self.h * 60 * 60 + self.m * 60 + self.s
            self.operation(seconds)
        elif len(args) == 1 and type(args[0]) is int:
            self.h = int(str(args[0])[:2])
            self.m = int(str(args[0])[2:4])
            self.s = int(str(args[0])[4:])
            seconds = self.h * 60 * 60 + self.m * 60 + self.s
            self.operation(seconds)
        elif len(args) == 3:
            self.h = args[0]
            self.m = args[1]
            self.s = args[2]
            seconds = self.h * 60 * 60 + self.m * 60 + self.s
            self.operation(seconds)
        else:
            self.h = 0
            self.m = 0
            self.s = 0

    def __init_with_instance(self, *args):
        o = args[0]
        self.h = o.h
        self.m = o.m
        self.s = o.s
        seconds = self.h * 60 * 60 + self.m * 60 + self.s
        self.operation(seconds)

    def __add__(self, other):
        seconds = (self.h + other.h) * 60 * 60 + (self.m + other.m) * 60 + self.s + other.s
        self.operation(seconds)
        return Time(
            self.h,
            self.m,
            self.s,
        )

    def __sub__(self, other):
        seconds = abs(self.h - other.h) * 60 * 60 + abs(self.m - other.m) * 60 + abs(self.s - other.s)
        self.operation(seconds)
        return Time(
            self.h,
            self.m,
            self.s,
        )

    def __mul__(self, other):
        seconds = (self.h * other * 60 * 60) + (self.m * other * 60) + self.s * other
        self.operation(seconds)
        return Time(
            self.h,
            self.m,
            self.s,
        )

    def operation(self, seconds):
        self.h = seconds // (60 * 60)
        self.m = (seconds - self.h * 60 * 60) // 60
        self.s = (seconds - self.h * 60 * 60) % 60

    def __eq__(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

    def __ne__(self, other):
        return self.h != other.h or self.m != other.m or self.s != other.s

    def __lt__(self, other):
        return (self.h * 60 * 60 + self.m * 60 + self.s) < (other.h * 60 * 60 + other.m * 60 + other.s)

    def __gt__(self, other):
        return (self.h * 60 * 60 + self.m * 60 + self.s) > (other.h * 60 * 60 + other.m * 60 + other.s)

    def __le__(self, other):
        return (self.h * 60 * 60 + self.m * 60 + self.s) <= (other.h * 60 * 60 + other.m * 60 + other.s)

    def __ge__(self, other):
        return (self.h * 60 * 60 + self.m * 60 + self.s) >= (other.h * 60 * 60 + other.m * 60 + other.s)

    def __str__(self):
        return f'Time is {self.h}:{self.m}:{self.s}'


t1 = Time('1:1:3')
t2 = Time('1:1:2')
print(f't1 == t2: {t1 == t2}')
print(f't1 != t2: {t1 != t2}')
print(f't1 > t2: {t1 > t2}')
print(f't1 < t2: {t1 < t2}')
print(f't1 >= t2: {t1 >= t2}')
print(f't1 <= t2: {t1 <= t2}')
print(f't1 * number: {t1 * 2}')
# print(t1 + t2)
# print(t1 - t2)
print(Time(Time(Time(Time(Time('13:6:23'))))))
print(Time(13, 6, 23))
print(Time('13:61:89'))
print(Time())
print(Time(1, 142, 53, 54))
print(Time(126583))
