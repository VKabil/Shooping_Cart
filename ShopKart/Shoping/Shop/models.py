from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFileName(request, fileName):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_fileName="%s%s"%(now_time,fileName)
    return os.path.join('uploads/',new_fileName)

class Catagory(models.Model):
    name =models.CharField(max_length=150, null=False,blank=False)
    images=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    
class Product(models.Model):
    catagory=models.ForeignKey(Catagory, on_delete=models.CASCADE)
    name =models.CharField(max_length=150, null=False,blank=False)
    vendor =models.CharField(max_length=150, null=False,blank=False)
    product_images=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name

