from django.shortcuts import render
from django.http import HttpRequest
from .models import Slider

def indexView(request: HttpRequest):

    sliders = Slider.objects.all()
    context = dict()

    if sliders:
        images = sliders[0].image_set.all()
        context['images'] = images 

    return render(request, "space_agency/index.html", context)