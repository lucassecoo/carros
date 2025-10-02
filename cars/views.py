from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cars.models import Car, Brand
from cars.forms import CarModelForm, BrandModelForm

class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains =search)
        return cars

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class NewBrandView(CreateView):
    model = Car.brand
    form_class = BrandModelForm
    template_name = 'new_brand.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

class CarDeleteView(DetailView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'