from django import forms
from  cars.models import Brand, Car

class CarModelForm(forms.ModelForm): #monta o form automaticamente de Car
    class Meta:
        model = Car
        fields = '__all__'

class BrandModelForm(forms.ModelForm): #monta o form automaticamente de Brand
    class Meta:
        model = Brand
        fields = '__all__'

    def clean_name(self): #função de django que valida se a marca ja existe no banco
        name = self.cleaned_data.get('name')
        if Brand.objects.filter(name__iexact=name).exists():
            self.add_error('name', 'Marca já está registrada!')
        return name