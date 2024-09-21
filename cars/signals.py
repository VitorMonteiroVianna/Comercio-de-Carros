from cars.models import Cars, CarInventory
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, pre_save
from django.db.models import Sum


def update_car_inventory():
    qnt_cars = Cars.objects.all().count()
    sum_cars_value = Cars.objects.aggregate(
        sum_value = Sum('value')
    )
    CarInventory.objects.create(
        cars_count = qnt_cars,
        cars_value = sum_cars_value['sum_value']
    )


@receiver(post_save, sender = Cars)
def cars_post_save(sender, instance, **kwargs):
    update_car_inventory()


@receiver(post_delete, sender = Cars)
def cars_post_delete(sender, instance, **kwargs):
    update_car_inventory()


@receiver(pre_save, sender=Cars)
def cars_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "O vendedor optou por não adicionar BIO"