from django.shortcuts import render
from django.http import HttpRequest

def indexView(request: HttpRequest):
    context = {
        "void": "void"   
	}
    return render(request, "space_agency/index.html", context)