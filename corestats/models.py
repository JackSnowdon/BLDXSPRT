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

class Combatant(models.Model):
    base = models.OneToOneField(
        BaseModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    current_hp = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)])
    
    def __str__(self):
        return self.base.name


class FightStat(models.Model):
    fight_name = models.CharField(max_length=50)
    fighter_limit = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    fighters = models.ManyToManyField('Combatant')

    def __str__(self):
        return self.fight_name

