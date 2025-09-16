from django.shortcuts import render, redirect
from cars.models import Car, Brand
from cars.forms import CarForm

def cars_view(request):
    search = request.GET.get('search')
    cars = Car.objects.all().order_by('model')

    if search:
        cars = cars.filter(model__icontains=search)#filtra pelo modelo do veiculo

    return render( #renderiza na url
        request,
        'cars.html',
        {'cars': cars}, #cars remete a classe Car dentro do banco de dados
    )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )