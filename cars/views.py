from django.shortcuts import render, redirect
from cars.models import Cars
from cars.forms import AddCarForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView



class CarsListView(ListView):
    model = Cars
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains = search)
        return cars


class AddCarCreateView(CreateView):
    model = Cars
    form_class = AddCarForm
    success_url = '/cars'
    template_name = 'add_cars.html'

