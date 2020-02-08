from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
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
                base.base_hp = strengh * (dex * speed)
                base.save()
                messages.error(request, 'Added {0}'.format(base.name), extra_tags='alert')
                return redirect("corehome")

    else:
        base_form = NewBaseForm()
    return render(request, "new_base.html", {"base_form": base_form })

