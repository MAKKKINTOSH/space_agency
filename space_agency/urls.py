from django.urls import path
from .views import indexView

app_name = "space_agency"

urlpatterns = [
    path("", indexView, name="index")
]