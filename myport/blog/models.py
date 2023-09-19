from django.db import models

# Starting og Blog Section 
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to ='blogpic',blank=True,null=True)  # pic must be 600x400
    image_small = models.ImageField(upload_to ='blogpic',blank=True,null=True) # pic must be 400x225
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title + ' by ' + self.author 
# # Create your models here.
# class Post(models.Model):
#     sno = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     author = models.CharField(max_length=13)
#     slug = models.CharField(max_length=130)
#     timeStamp = models.DateTimeField(blank=True)
    
#     def __str__(self):
#         return self.title + ' by ' + self.author 
    