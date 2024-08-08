from django import forms    
from cars.models import Brand


class AddCarForm(forms.Form):
    brand = forms.ModelChoiceField(Brand.objects.all())
    model = forms.CharField(max_length=255)
    color = forms.CharField(max_length=55)
    factory_yaer = forms.IntegerField()
    model_yaer = forms.IntegerField()
    value = forms.FloatField()
    image = forms.ImageField()