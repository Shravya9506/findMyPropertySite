from .forms import PropertyMessageForm
from django.shortcuts import redirect, render
from .models import *



def message_owner(request, propertyId):
    property = Property.objects.filter(pk=propertyId)
    print(request)
    seller = Seller.objects.filter(user__id = request.user.id)
    if request.method == "POST":
        form = PropertyMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.property = property
            message.save()
            return redirect('properties:message_recorded')
    else:
        form = PropertyMessageForm()
    return render(request, 'message.html', {'form': form})