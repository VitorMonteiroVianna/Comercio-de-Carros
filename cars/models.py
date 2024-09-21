from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    
    def __str__(self):
        return self.brand


class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, default=None)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=55)
    factory_yaer = models.IntegerField(null=True, blank=True)
    model_yaer = models.IntegerField(null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="cars", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.model} --> ID '{self.id}'"


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at'] #Ordena pela coluna create at, DESC (-)
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'