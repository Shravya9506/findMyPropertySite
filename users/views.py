from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.utils import timezone
from .models import *
from .forms import *

now = timezone.now()

def register_customer(request):
    if request.method == 'POST':
        registered_as = request.POST.get('register_as', '')
        is_buyer = True if registered_as == 'BU' else False
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save(is_buyer)
            return redirect('users:login')
    args = {}
    args.update(csrf(request))
    args['form'] = CustomerSignUpForm()
    return render(request, 'registration/signup.html', args)


@login_required
def edit_profile(request):
    customer = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('findMyProperty:home')
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'registration/edit_customer.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html',
                  {'login': login})


