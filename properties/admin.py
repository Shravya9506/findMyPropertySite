from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.admin import UserAdmin
from .models import Property, CustomerFavoriteProperty


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'sale_type', 'created', 'available')


class CustomerFavoritesList(admin.ModelAdmin):
    list_display = ('id', 'buyer_username', 'property_name', 'seller_username')

    def buyer_username(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.buyer.user.username
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def seller_username(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.property.seller
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def property_name(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.property.name
        except ObjectDoesNotExist:
            return 'ERROR!!'

admin.site.register(Property, PropertyAdmin)
admin.site.register(CustomerFavoriteProperty, CustomerFavoritesList)
