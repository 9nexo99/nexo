from django.db import models

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)
