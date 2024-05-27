from django.db import models
class Main(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
class HR(models.Model):
    HR_id = models.AutoField(primary_key=True)
    id=models.ForeignKey(Main,on_delete=models.CASCADE)
    subtype=models.CharField(max_length=100)
    content = models.TextField()
class DEV(models.Model):
    DEV_id = models.AutoField(primary_key=True)
    id=models.ForeignKey(Main,on_delete=models.CASCADE)
    subtype=models.CharField(max_length=100)
    content = models.TextField()
class SALES(models.Model):
    SALES_id = models.AutoField(primary_key=True)
    id=models.ForeignKey(Main,on_delete=models.CASCADE)
    subtype=models.CharField(max_length=100)
    content = models.TextField()
# Create your models here.