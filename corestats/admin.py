from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BaseModel)
admin.site.register(Combatant)
admin.site.register(FightStat)
