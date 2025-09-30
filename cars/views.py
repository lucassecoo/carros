from django.shortcuts import render, redirect
from django.views import View

from cars.models import Car, Brand
from cars.forms import CarModelForm, BrandModelForm

class CarsViews(View):

    def get(self, request):
        search = request.GET.get('search')
        cars = Car.objects.all().order_by('model')

        if search:
            cars = cars.filter(model__icontains=search)  # filtra pelo modelo do veiculo

        return render(  # renderiza na url
            request,
            'cars.html',
            {'cars': cars},  # cars remete a classe Car dentro do banco de dados
        )

class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )


def new_brand_view(request):
    if request.method == 'POST':
        new_brand_form = BrandModelForm(request.POST, request.FILES)
        if new_brand_form.is_valid():
            new_brand_form.save()
            return redirect('cars_list')
    else:
        new_brand_form = BrandModelForm()
    return render(
        request,
        'new_brand.html',
        {'new_brand_form': new_brand_form}
    )