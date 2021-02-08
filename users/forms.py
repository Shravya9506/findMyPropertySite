from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Buyer, Seller


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password1', 'password2')

    def save(self, is_buyer):
        user = super().save(commit=False)
        if is_buyer:
            user.is_buyer = True
            user.save()
            Buyer.objects.create(user=user)
        else:
            user.is_seller = True
            user.save()
            Seller.objects.create(user=user)
        return user


class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')


