from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cars.views import CarsView, AddCarsView
from accounts.views import register_view, authenticate_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', CarsView.as_view(), name='cars_list'),
    path('cars/add', AddCarsView.as_view(), name='add_car'),
    path('user/register', register_view, name='register_user'),
    path('user/auth', authenticate_view, name='authenticate_user'),
    path('user/logout', logout_view, name='logout_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

