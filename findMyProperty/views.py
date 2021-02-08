from django.shortcuts import redirect, render
from properties.models import Property
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties' : properties})