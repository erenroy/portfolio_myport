from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Messagge from ' + self.name 

class files(models.Model):
    file_title = models.CharField(max_length=255)
    file = models.FileField(upload_to="files")

class Myprojects(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mydesc = models.CharField(max_length=455)
    proimage = models.ImageField(upload_to ='projectpic',blank=True,null=True)