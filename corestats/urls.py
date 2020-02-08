from django.urls import path
from .views import *

urlpatterns = [
    path('corehome/', corehome, name="corehome"),
    path('new_base/', new_base, name="new_base"),
    path('setup_fight/', setup_fight, name="setup_fight"),
    path(r'delete_base/<pk>', delete_base, name="delete_base"),
    path(r'view_base/<pk>', view_base, name="view_base"),
    path('new_combatant/', new_combatant, name="new_combatant"),
]