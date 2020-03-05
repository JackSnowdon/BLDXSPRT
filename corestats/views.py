from django.contrib import messages
from django.shortcuts import redirect, render, reverse, get_object_or_404
from .models import *
from .forms import *

# Create your views here.


from django.shortcuts import render

# Create your views here.

def corehome(request):
    chars = BaseModel.objects.order_by("name")
    return render(request, "corehome.html", {"chars": chars})

def new_base(request):
    if request.method == "POST":
        base_form = NewBaseForm(request.POST)
        if base_form.is_valid():
            base = base_form.save(commit=False)
            base.heart = 0
            strengh = int(request.POST.get('strengh'))
            speed = int(request.POST.get('speed'))
            social = int(request.POST.get('social'))
            intel = int(request.POST.get('intel'))
            dex = int(request.POST.get('dex'))
            
            stat_total = strengh + speed + social + intel + dex

            if stat_total > 100:
                messages.error(request, 'Invalid Stats for {0}, stat total ({1}) greater than 100'.format(base.name, stat_total), extra_tags='alert')
            else:
                base.base_hp = strengh * (dex + speed)
                base.save()
                messages.error(request, 'Added {0}'.format(base.name), extra_tags='alert')
                return redirect("corehome")

    else:
        base_form = NewBaseForm()
    return render(request, "new_base.html", {"base_form": base_form })


def view_base(request, pk):
    base = get_object_or_404(BaseModel, id=pk)
    return render(request, "view_base.html", {"base": base })


def delete_base(request, pk):
    base = get_object_or_404(BaseModel, id=pk)
    messages.error(request, 'Deleted {0}'.format(base.name), extra_tags='alert')
    base.delete()
    return redirect(reverse('corehome'))


def setup_fight(request):
    fighters = Combatant.objects.all()
    return render(request, "setup_fight.html", {"fighters": fighters })


def new_combatant(request):
    if request.method == "POST":
        combatant_form = AddToCombat(request.POST)
        if combatant_form.is_valid():
            current_hp = int(request.POST.get('current_hp'))
            pk = request.POST.get('base')
            combatant = get_object_or_404(BaseModel, pk=pk)
            maxhp = combatant.base_hp
            if current_hp <= maxhp:
                combatant_form.save()
                messages.error(request, 'Added {0} to combat'.format(combatant.name), extra_tags='alert boldest')
                return redirect(reverse('setup_fight'))
            else:
                messages.warning(request, 'Your current HP can not exceed your Max HP! ({0} HP)'.format(maxhp), extra_tags='alert')
    else:
        combatant_form = AddToCombat()
    return render(request, 'new_combatant.html', {'combatant_form': combatant_form })