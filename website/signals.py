from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer

def customerProfile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(
            user = instance,
            name = instance.username,
            email= instance.email,
            )



post_save.connect(customerProfile, sender=User)