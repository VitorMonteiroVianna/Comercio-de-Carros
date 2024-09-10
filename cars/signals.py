from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Cars


@receiver(pre_save, sender=Cars)
def car_pre_save(sender, instance, **kwargs):
    print("TESTE DE PRE SAVE EM CARRO") 
    
@receiver(pre_delete, sender=Cars)
def car_pre_delete(sender, instance, **kwargs):
    print("TESTE DE PRE DELETE EM CARRO") 
    
@receiver(post_save, sender=Cars)
def car_post_save(sender, instance, **kwargs):
    print("TESTE DE POST SAVE EM CARRO") 
    
@receiver(post_delete, sender=Cars)
def car_post_delete(sender, instance, **kwargs):
    print("TESTE DE POST DELETE EM CARRO") 
