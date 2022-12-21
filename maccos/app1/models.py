from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_number = models.IntegerField(max_length=10)
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.product_name
