from django import forms    
from cars.models import Cars


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"
        
    def clean_model_yaer(self):
        model_yaer = self.cleaned_data.get('model_yaer')
        if model_yaer < 1900:
            self.add_error('model_yaer', 'Não é possivel adicionar carros de antes de 1900')
        return model_yaer
