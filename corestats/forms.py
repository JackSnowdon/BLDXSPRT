from django import forms

from .models import *

class NewBaseForm(forms.ModelForm):

    class Meta:
        model = BaseModel
        exclude = ['heart', 'base_hp']
        labels = {
            "dex": "Dexterity",
        }


class AddToCombat(forms.ModelForm):

    class Meta:
        model = Combatant
        fields = '__all__'
        labels = {
            "base": "Combatant",
            "current_hp": "Current HP"
        }
        
