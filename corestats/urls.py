from django.urls import path
from .views import *

urlpatterns = [
    path('corehome/', corehome, name="corehome"),
    path('new_base/', new_base, name="new_base"),
]