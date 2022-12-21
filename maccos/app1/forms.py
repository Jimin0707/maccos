from django.core import validators
from django import forms
from .models import Product

class ProductData(forms.ModelForm):
    class Meta:
        model = Product
        fiels = ['product_id','product_name','product_desc']
