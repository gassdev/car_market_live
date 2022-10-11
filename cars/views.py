from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.core.paginator import Paginator

from .models import Car

def cars(request: HttpRequest):
    cars = Car.objects.order_by('-created_at').all()
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    search_fields = Car.objects.values('brand', 'model', 'year')
    context = {
        'cars':paged_cars,
        'search_fields':search_fields,
    }
    return render(request, 'cars/cars.html', context)

def car_details(request: HttpRequest, id):
    single_car = get_object_or_404(Car, pk=id)
    
    context = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_details.html', context)

def search(request: HttpRequest):
    cars = Car.objects.order_by('created_at')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
            
    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            cars = cars.filter(brand__iexact=brand)
            
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
            
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
    
    search_fields = Car.objects.values('brand', 'model', 'year', 'condition')
    context = {
        'cars': cars,
        'search_fields': search_fields,
    }
    return render(request, 'cars/search.html', context)