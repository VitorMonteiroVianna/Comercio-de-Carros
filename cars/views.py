from django.shortcuts import render
from cars.models import Cars


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