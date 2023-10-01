from django import forms
from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError


#класс с полями форм
class AdvertisementForm(ModelForm):
    class Meta:
     model = Advertisement
     fields = "__all__"
     widgets = {
        'title' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        'description' : forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        'price' : forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
        'auction' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'image' : forms.FileInput(attrs={'class': 'form-control form-control-lg'})
     }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0]=="?":
            raise forms.ValidationError("нельзя начинать с этого знака!")
        return title
       
     

    