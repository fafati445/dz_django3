from tkinter.constants import CASCADE

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    model = models.CharField(max_length=200,default=None)
    year = models.DateField(default=None)
    color = models.CharField(max_length=200,default=None)
    mileage = models.IntegerField(default=None)
    volume = models.IntegerField(default=None)
    body_type = models.CharField(max_length=200,default=None)
    drive_unit = models.CharField(max_length=200,default=None)
    gearbox = models.CharField(max_length=200,default=None)
    fuel_type = models.CharField(max_length=200,default=None)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=None)
    image = models.ImageField(default=None)


class Sale(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    client = models.ForeignKey(Client,on_delete= models.CASCADE,related_name='client',default=None)
    car = models.ForeignKey(Car,on_delete= models.CASCADE,related_name='car',default=None)
    created_at = models.DateField(default=None)
