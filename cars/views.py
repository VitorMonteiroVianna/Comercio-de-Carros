from django.shortcuts import render
from cars.models import Cars


def cars_view(request):
    cars = Cars.objects.all()
    
    return(
        render(
            request,
            'cars.html',
            {"cars" : cars}
        )
    )