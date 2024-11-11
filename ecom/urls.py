# ecom/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base_view, name='base'),  # This will point to your homepage
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
