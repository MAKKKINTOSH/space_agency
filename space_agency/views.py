from django.shortcuts import render
from django.http import HttpRequest
from .models import Image

def indexView(request: HttpRequest):

    images = Image.objects.all()
    print(images)
    context = {
        "images": images 
	}

    return render(request, "space_agency/index.html", context)