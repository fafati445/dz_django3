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
    model = models.CharField(max_length=200)
    year = models.DateField()
    color = models.CharField(max_length=200)
    mileage = models.IntegerField()
    volume = models.IntegerField()
    body_type = models.CharField(max_length=200,choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField(max_length=200,choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(max_length=200,choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(max_length=200,choices=FUEL_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField()


class Sale(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    client = models.ForeignKey(Client,on_delete= models.CASCADE,related_name='client')
    car = models.ForeignKey(Car,on_delete= models.CASCADE,related_name='car')
    created_at = models.DateField()
