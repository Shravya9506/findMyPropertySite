from django.shortcuts import redirect, render
from properties.models import Property, CustomerFavoriteProperty
from django.shortcuts import get_object_or_404
from users.models import Buyer, Seller
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    properties = Property.objects.all()
    if request.user.id == None:
        return render(request, 'home.html', {'properties' : properties})
    elif Seller.objects.filter(user_id=request.user.id).values_list('user_id', flat=True).distinct().count() > 0:
        return redirect('properties:view_your_properties', request.user.id)
    else:
        buyer = get_object_or_404(Buyer, user_id=request.user.id)
        favs = CustomerFavoriteProperty.objects.filter(buyer=buyer).values_list('property_id', flat=True).distinct()
        print(list(favs))
        return render(request, 'look_up_property.html', {'properties': properties, 'favorites': list(favs)})

def about_us(request):
    return render(request, 'about_us.html')
