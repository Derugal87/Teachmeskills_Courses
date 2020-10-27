class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed


    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    def raise_speed(self) -> None:
        self.__speed = self.speed + 5

    def reduce_speed(self) -> None:
        self.__speed = self.speed - 5

    def stop(self) -> None:
        self.__speed = 0

    def reversal(self) -> None:
        self.__speed = self.speed * (-1)


car = Car('Mazda', '6', 2003)
print(car.__getattribute__('speed'))
car.raise_speed()
car.raise_speed()
print(car.__getattribute__('speed'))
car.reduce_speed()
print(car.__getattribute__('speed'))
car.stop()
print(car.__getattribute__('speed'))
car.raise_speed()
car.reversal()
print(car.__getattribute__('speed'))

