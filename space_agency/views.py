from django.shortcuts import render
from django.http import HttpRequest
from .models import Slider

def indexView(request: HttpRequest):

    images = Slider.objects.all()[0].image_set.all()
    print(f"IMAGES {images}")
    context = {
        "images": images 
	}

    return render(request, "space_agency/index.html", context)