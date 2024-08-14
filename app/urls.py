from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cars.views import cars_view, add_cars_view
from accounts.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', cars_view, name='cars_list'),
    path('cars/add', add_cars_view, name='add_car'),
    path('register', register_view, name='register_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

