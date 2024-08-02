from django.shortcuts import render, HttpResponse
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

# def cars_view(request):
#     cars = Cars.objects.filter(model = 'C4')
#     for car in cars:
#         return HttpResponse(car.image.url)