from django.db import models
from   django.contrib.auth.models   import    User 
# Create your models here.

class   Category(models.Model):
    name   =  models.CharField(max_length =  255)
    class  Meta  :
        verbose_name_plural =  'Categories'

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    