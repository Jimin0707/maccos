from django.core import validation
from django import form
from models import user

class productRegistration(forms.ModelForm):
    
    class Meta:
        model = user
        fields = ("id","name","description")
        widgets={
            'product_id': forms.TextInput(attrs={'class':'forms-control'}),
            'name': forms.TextInput(attrs={'class':'forms-control'}),
            'description': forms.TextInput(attrs={'class':'forms-control'}),
        }