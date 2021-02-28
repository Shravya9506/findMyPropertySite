from .forms import PropertyMessageForm, PropertyForm
from django.shortcuts import redirect, render
from .models import *
from users.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from io import BytesIO
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.http import HttpResponse
from django.conf import settings


@login_required
def add_property(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = seller
            property.save()
            return redirect('findMyProperty:home')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

@login_required
def view_your_properties(request, pk):
    properties = Property.objects.filter(seller_id =pk)
    return render(request, 'view_your_properties.html', {'properties': properties})

@login_required
def view_messages_received(request, pk):
    propertyMessages = PropertyMessage.objects.filter(seller_id =pk)
    return render(request, 'view_messages_received.html', {'propertyMessages': propertyMessages})

@login_required
def edit_property(request, pk):
    property = get_object_or_404(Property, pk =pk)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=False)
            property.save()
            return redirect('properties:view_your_properties')
        else:
            form = PropertyForm(instance=property)
            return render(request, 'edit_properties.html', {'form': form})

@login_required
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        property.delete()
        return redirect('properties:view_your_properties')
    else:
        return render(request, 'delete_properties.html', {'property': property})

def message_owner(request, propertyId):
    property = get_object_or_404(Property, pk=propertyId)
    sellerId = Property.objects.filter(id=propertyId).values('seller').first()
    seller = get_object_or_404(Seller, pk = sellerId['seller'])
    if request.method == "POST":
        form = PropertyMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.property = property
            message.seller = seller
            message.save()
            return render(request, 'message_recorded.html')
    else:
        form = PropertyMessageForm()
    return render(request, 'message.html', {'form': form})

@login_required
def mark_as_favorite(request, pk):
    buyer = get_object_or_404(Buyer, user_id=request.user.id)
    property = get_object_or_404(Property, id=pk)
    CustomerFavoriteProperty.objects.create(buyer=buyer, property=property)
    favs = CustomerFavoriteProperty.objects.filter(buyer=buyer).values('property_id')
    properties = Property.objects.filter(id__in= [fav['property_id'] for fav in favs])
    return render(request,'view_your_favorites.html', {'properties':properties})

@login_required
def unmark_as_favorite(request, pk):
    buyer = get_object_or_404(Buyer, user_id=request.user.id)
    property = get_object_or_404(Property, id=pk)
    CustomerFavoriteProperty.objects.filter(buyer=buyer, property=property).delete()
    favs = CustomerFavoriteProperty.objects.filter(buyer=buyer).values('property_id')
    properties = Property.objects.filter(id__in=[fav['property_id'] for fav in favs])
    return render(request, 'view_your_favorites.html', {'properties': properties})

@login_required
def view_your_favorites(request, pk):
    buyer = get_object_or_404(Buyer, user_id=request.user.id)
    favs = CustomerFavoriteProperty.objects.filter(buyer=buyer).values('property_id')
    properties = Property.objects.filter(id__in=[fav['property_id'] for fav in favs])
    return render(request, 'view_your_favorites.html', {'properties': properties})


@login_required
def look_up_property(request, pk):
    buyer = get_object_or_404(Buyer, user_id=request.user.id)
    properties = Property.objects.all()
    favs = CustomerFavoriteProperty.objects.filter(buyer=buyer).values_list('property_id', flat=True).distinct()
    print(list(favs))
    return render(request, 'look_up_property.html', {'properties' : properties, 'favorites' : list(favs)})


@login_required
def property_pdf_email(request, pk):
    property = get_object_or_404(Property, id=pk)
    buyer = get_object_or_404(Buyer, user_id=request.user.id)
    # create invoice e-mail
    subject = 'Details of the property - {}'.format(property.name)
    message = 'Hello {},\n' \
              'Please find the attachment for the e-copy of the property you are interested in. \n' \
              'Contact us in case you need assistance of any sort, our team is happy to assist you. \n' \
              'Team Find my property'.format(buyer.user.first_name)
    email = EmailMessage(subject,
                         message,
                         'admin@findmyproperty.com',
                         [buyer.user.email])

    html = render_to_string('property_pdf.html',
                            { 'property' :property})
    out = BytesIO()
    HTML(string=html,base_url=request.build_absolute_uri()).write_pdf(out,
                                stylesheets=[CSS(settings.STATIC_ROOT + '/css/pdf.css')])
    email.attach('Property_{}.pdf'.format(property.name),
                 out.getvalue(),
                 'application/pdf')
    #send e-mail
    email.send()
    return render(request, 'pdf_sent.html')