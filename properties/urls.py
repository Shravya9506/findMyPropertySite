from . import views
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views



app_name = 'properties'

urlpatterns = [
    path('send_message/<int:propertyId>', views.message_owner, name='message_owner'),
    path('add_property/<int:pk>', views.add_property, name='add_property'),
    path('view_your_properties/<int:pk>', views.view_your_properties, name='view_your_properties'),
    path('view_messages_received/<int:pk>', views.view_messages_received, name='view_messages_received'),
    path('edit_property/<int:pk>', views.edit_property, name='edit_property'),
    path('delete_property/<int:pk>', views.delete_property, name='delete_property'),
    path('mark_as_favorite/<int:pk>', views.mark_as_favorite, name='mark_as_favorite'),
    path('unmark_as_favorite/<int:pk>', views.unmark_as_favorite, name='unmark_as_favorite'),
    path('view_your_favorites/<int:pk>', views.view_your_favorites, name='view_your_favorites'),
    path('look_up_property/<int:pk>', views.look_up_property, name='look_up_property'),
    path('property_pdf_email/<int:pk>', views.property_pdf_email, name='property_pdf_email'),
]