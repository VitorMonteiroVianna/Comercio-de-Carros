from django.shortcuts import render, HttpResponse, redirect
from cars.models import Cars
from cars.forms import AddCarForm


def cars_view(request):
    search = request.GET.get('search')

    if search:
        cars = Cars.objects.filter(model__icontains = search)
    else: 
        cars = Cars.objects.all()
    
    return(
        render(
            request,
            'cars.html',
            {"cars" : cars}
        )
    )


def add_cars_view(request):
    if request.method == 'POST':
        add_car_form = AddCarForm(request.POST, request.FILES)
        if add_car_form.is_valid():
            add_car_form.save()
            return redirect('cars_list')
    
    else:
        add_car_form = AddCarForm()
    
    return(
        render(
            request,
            'add_cars.html',
            {"add_car_form" : add_car_form}
        )
    )