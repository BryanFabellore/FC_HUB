from django.db import models

# Create your models here.
class invtry(models.Model):
    invtry_prdctName = models.CharField(max_length=250)
    invtry_color = models.CharField(max_length=250)
    invtry_prdctBnldType = models.CharField(max_length=250)
    invtry_prdctPrice = models.DecimalField(decimal_places=3,max_digits=10)
    invtry_prdctLength = models.DecimalField(decimal_places=3,max_digits=10)
    invtry_qty = models.IntegerField()
    
    