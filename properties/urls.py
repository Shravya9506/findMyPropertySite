from . import views
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views



app_name = 'properties'

urlpatterns = [
    path('send_message/<int:propertyId>', views.message_owner, name='message_owner'),
]