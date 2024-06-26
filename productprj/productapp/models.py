from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()


    def __str__(self):
        return self.name
    
    class Meta:
        db_table='productapp_product'
        
