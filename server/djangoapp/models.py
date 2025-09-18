from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.TextField()
    foundedYear = models.IntegerField(default=2025,
        validators=[MaxValueValidator(2026),MinValueValidator(1900)]
        )

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('PICKUP', 'Pick-up'),
        ('HATCH', 'Hatchback'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[MaxValueValidator(2026),MinValueValidator(2005)]
        )
    top_speed = models.IntegerField(default=100,
        validators=[
            MaxValueValidator(400),
            MinValueValidator(50)
        ])
    FUEL_TYPES = [
        ('GASOLINE', 'Gasoline'),
        ('ELECTRIC', 'Electric'),
        ('HYBRID', 'Hybrid'),
        ('DIESEL', 'Diesel'),
        ('FLEX', 'Flex'),
    ]
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES, default='GASOLINE')
    
    def __str__(self):
        return self.name  # Return the name as the string representation