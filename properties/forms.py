from django import forms
from .models import *

class PropertyMessageForm(forms.ModelForm):
    class Meta:
        model = PropertyMessage
        fields = ('message', 'email', 'phone')

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('name', 'description', 'price', 'address', 'city', 'state', 'zipcode','sale_type', 'purchase_type')

