from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ItemDetails(models.Model):
    price=models.FloatField()
    length=models.CharField(max_length=10)
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150)
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)
    
    
class cart(models.Model):
    Id_product=models.IntegerField()
    Id_user=models.IntegerField()
    image=models.CharField(max_length=150)
    price=models.FloatField()
    qty=models.IntegerField()
    length=models.CharField(max_length=10)
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    Created_at=models.DateTimeField(auto_now_add=True)