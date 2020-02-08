from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    base_hp = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])
    strengh = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    speed = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    social = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    intel = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    dex = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    heart = models.IntegerField()
    
    def __str__(self):
        return self.name


