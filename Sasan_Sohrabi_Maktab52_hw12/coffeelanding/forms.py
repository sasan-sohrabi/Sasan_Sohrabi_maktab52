from django import forms
from django.core.exceptions import ValidationError
from .models import Menu_items


def name_validator(value: str) -> None:
    if not value.istitle():
        raise ValidationError("Menu item name must be title!!!!")

def price_validator(value: int) -> None:
    if value < 0:
        raise ValidationError("Price must be positive!!!!")

def discount_validator(value: int) -> None:
    if value < 0:
        raise ValidationError("Discount must be positive!!!!")



# Define form for menuitem
class MenuForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=10, validators=[name_validator], label='Name of Product')
    price = forms.IntegerField(validators=[price_validator], label='Price')
    discount = forms.IntegerField(validators=[discount_validator], label='Discount')
    category = forms.IntegerField(label='Category')
    # date_serve = forms.DateField(label='Date Serve', required=False)
    # time = forms.TimeField(label='Time need to prepare')
    available = forms.BooleanField(label='available')
    image = forms.FileField(label='Image')

class MenuForm2(forms.ModelForm):
    class Meta:
        model = Menu_items
        fields = '__all__'

        widgets = {
            'name': forms.TextInput({'class': 'form-control'}),
            'date_serve': forms.DateInput({'class': 'form-control'}),
            'cooking_time_estimate': forms.TimeInput({'class': 'form-control'}),
            'available': forms.CheckboxInput({'class': 'form-control'}),
            'category_id': forms.Select({'class': 'form-control'}),
        }