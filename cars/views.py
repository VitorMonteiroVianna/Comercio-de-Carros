from django.shortcuts import render, redirect
from cars.models import Cars
from cars.forms import AddCarForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



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


@method_decorator(login_required(login_url = '/user/auth'), name='dispatch')
class AddCarCreateView(CreateView):
    model = Cars
    form_class = AddCarForm
    success_url = '/cars'
    template_name = 'add_cars.html'
    

@method_decorator(login_required(login_url = '/user/auth'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Cars
    form_class = AddCarForm
    template_name = 'car_update.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs = {'pk': self.object.pk})


@method_decorator(login_required(login_url = '/user/auth'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Cars
    template_name = 'car_delete.html'
    success_url ='/cars'