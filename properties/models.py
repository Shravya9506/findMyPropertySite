from django.db import models
from django.urls import reverse
from users.models import Seller, Buyer

class Property(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, related_name='seller', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)
    NEW = 'NE'
    RESALE = 'RE'
    BLANK = ''
    sale_type_options = (
        (BLANK, ''),
        (NEW, 'New property'),
        (RESALE, 'Resale'),
    )
    sale_type = models.CharField(max_length=2, choices=sale_type_options, default=BLANK)
    LEASE = 'LE'
    OWN = 'OW'
    RENT = 'RE'
    purchase_type_options=(
        (LEASE, 'Lease the property'),
        (OWN, 'Own the property'),
        (RENT, 'Rent the property')
    )
    purchase_type = models.CharField(max_length=2, choices=purchase_type_options, default=LEASE)

    def __str__(self):
        return self.name


class CustomerFavoriteProperty(models.Model):
    buyer  =models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='buyer')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property')

    class Meta:
        unique_together = (('buyer', 'property'),)

    def __str__(self):
        return self.buyer.user.username + " likes " + self.property.name

class PropertyMessage(models.Model):
    message = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10, null=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller_details')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_details')
