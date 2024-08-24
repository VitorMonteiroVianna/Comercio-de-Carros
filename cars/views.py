from django.shortcuts import render, redirect
from cars.models import Cars
from cars.forms import AddCarForm
from django.views import View
from django.views.generic import ListView



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


class AddCarsView(View):
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('authenticate_user')
        
        add_car_form = AddCarForm()
        return(
            render(
                request,
                'add_cars.html',
                {"add_car_form" : add_car_form}
            )
        )
    
    def post(self, request):
        add_car_form = AddCarForm(request.POST, request.FILES)
        if add_car_form.is_valid():
            add_car_form.save()
            return redirect('cars_list')
        
        return(
            render(
                request,
                'add_cars.html',
                {"add_car_form" : add_car_form}
            )
        )
