from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cars.views import CarsListView, AddCarCreateView, CarDetailView
from accounts.views import register_view, authenticate_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', CarsListView.as_view(), name='cars_list'),
    path('cars/detail/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('cars/add', AddCarCreateView.as_view(), name='add_car'),
    path('user/register', register_view, name='register_user'),
    path('user/auth', authenticate_view, name='authenticate_user'),
    path('user/logout', logout_view, name='logout_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

