from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path(r'^filer/', include('filer.urls')),
    path('', include("space_agency.urls"))
]
