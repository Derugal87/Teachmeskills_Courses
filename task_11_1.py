import datetime



class Dog:
    def __init__(self, name, breed, age):
        self.__name = name
        self.__breed = breed
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, new_breed):
        self.__breed = new_breed

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def bark(self):
        return 'Bark!!!'

    def run(self):
        return 'Run!!!'


dog = Dog('Sharik', 'Alopekis', 5)
dog.name = 'Tuzik'
print(dog.name)
dog.breed = 'Akita'
print(dog.breed)
dog.__setattr__('age', 15)
print(dog.age)
dog.__setattr__('name', 'Vasya')
print(dog.__getattribute__('name'))
print(dog.bark())
print(dog.run())




class Cat:
    def __init__(self, name, breed, age):
        self.__name = name
        self.__breed = breed
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, new_breed):
        self.__breed = new_breed

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def myow(self):
        return 'Myow!!!'

    def run(self):
        return 'Run!!!'


class Car:
    def __init__(self, brand, colour, year):
        self.__brand = brand
        self.__colour = colour
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, new_colour):
        self.__colour = new_colour

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    def raise_speed(self):
        return 'Raise speed!!!'

    def reduce_speed(self):
        return 'Reduce speed!!!'


class House:
    def __init__(self, size, address, year):
        self.__size = size
        self.__address = address
        self.__year = year

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    def destroy(self):
        return 'It\'s destroyed!'

    def re_colour(self):
        return 'Let\'s recolour!'


class Clock:
    def __init__(self, brand, size, year):
        self.__brand = brand
        self.__size = size
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    def whatistime(self):
        return datetime.datetime.now()

    def how_to_buy_new(self):
        return 'Break old one, buy new one'