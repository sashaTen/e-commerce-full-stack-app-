from django.db import models
from django.contrib.auth.models   import  User 
from item.models   import    Item
from    django.utils   import timezone
# Create your models here.
class    CommentModel(models.Model):
    user   =  models.ForeignKey(User ,   on_delete=models.CASCADE)
    item   =  models.ForeignKey(Item,    on_delete =    models.CASCADE)
    timestamp =  models.TimeField(default  = timezone.now)
    text   =   models.TextField()


