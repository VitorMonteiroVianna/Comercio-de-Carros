from django.shortcuts import render, redirect
from cars.models import Cars
from cars.forms import AddCarForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



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


class CarDetailView(DetailView):
    model = Cars
    template_name = 'car_detail.html'


class AddCarCreateView(CreateView):
    model = Cars
    form_class = AddCarForm
    success_url = '/cars'
    template_name = 'add_cars.html'


class CarUpdateView(UpdateView):
    model = Cars
    form_class = AddCarForm
    template_name = 'car_update.html'
    success_url = '/cars'


class CarDeleteView(DeleteView):
    model = Cars
    template_name = 'car_delete.html'
    success_url ='/cars'