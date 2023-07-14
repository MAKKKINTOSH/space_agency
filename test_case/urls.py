from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path(r'^filer/', include('filer.urls')),
    path('', include("space_agency.urls"))
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
