from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    def __str__(self):
        return self.name


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete = models.CASCADE,null = True, blank = False) 
    item_name = models.CharField(max_length = 50, null = True, blank = False)
    total_quantity = models.IntegerField(default = 0)
    issued_quantity = models.IntegerField(default = 0)
    received_quantity = models.IntegerField(default = 0)
    unit_price = models.IntegerField(default = 0)

    def __str__(self):
        return self.item_name
    
    class Meta:
        ordering = ('-id',)

  

class Sale(models.Model):
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    amount_received = models.IntegerField(default = 0)
    issued_to = models.CharField(max_length = 50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0)

    @property
    def get_total(self):
       total = self.quantity * self.item.unit_price
       return int(total)
    
    @property
    def get_change(self):
        amount_received = self.amount_received
        total_sales = (self.quantity * self.item.unit_price)
        change =  amount_received - total_sales
        if amount_received < total_sales:
            return f'-{abs(int(change))}'
        else:
            return abs(int(change))

    
    def __str__(self):
        return self.item.item_name
    
    class Meta:
        ordering = ('-id',)
