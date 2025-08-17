from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    phone= models.CharField(max_length=15 )
    message=models.TextField(max_length=4000)
    image=models.FileField(upload_to="profile/",max_length=250,null=True,default=None)
