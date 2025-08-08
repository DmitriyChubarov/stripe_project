from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    item = models.ManyToManyField(Item)

    def __str__(self) -> str:
        return f"Order #{self.id} ({self.item.count()} items)"
    
    def total_amount(self):
        return (sum(i.price for i in self.item.all())) / 100