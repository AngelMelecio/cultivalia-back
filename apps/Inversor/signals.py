from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inversor
from apps.CodigoReferido.models import CodigoReferido

@receiver(post_save, sender=Inversor)
def create_referido_code(sender, instance, created, **kwargs):
    print('Signal!!')
    if created:
        CodigoReferido.objects.create(inversor=instance)