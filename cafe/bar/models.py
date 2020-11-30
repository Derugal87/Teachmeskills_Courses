from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    salary = models.FloatField(default=0.0)


class Reward(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    foundation_date = models.DateTimeField()


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=9)
    age = models.IntegerField(default=0)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class RewardEmployee(models.Model):
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reward_date = models.DateTimeField()


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=9)


class Menu(models.Model):
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    price = models.FloatField(default=0.0)
