from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, 
                on_delete=models.CASCADE)  # Many-to-one relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('SPORTS', 'Sports Car')
    ]
    type = models.CharField(max_length=12, 
            choices=CAR_TYPES, default='SUV') 
    year = models.IntegerField(default=2023,
    validators=[
        MaxValueValidator(2023),
        MinValueValidator(2015)
    ])
    # Other fields as needed
    def __str__(self):
        return self.name  # Return the name as the string representation