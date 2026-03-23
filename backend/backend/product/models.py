from django.db import models
from mptt.models import MPTTModel , TreeForeignKey

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self",on_delete=models.PROTECT,null=True,blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=100)


