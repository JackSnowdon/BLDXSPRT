from django import forms

from .models import *

class NewBaseForm(forms.ModelForm):

    class Meta:
        model = BaseModel
        exclude = ['heart', 'base_hp']
        labels = {
            "dex": "Dexterity",
        }
        
