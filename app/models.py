from django.db import models

class page(models.Model):
    Title=models.CharField(max_length=30,blank=True,null=True)
    Content=models.TextField(max_length=5000,blank=True,null=True)
    Created_on=models.DateTimeField(auto_now=False,auto_now_add=True)
    Thumbnail=models.ImageField(upload_to='thumbnail/')
    dp=models.FileField(upload_to='dp/')
    Author=models.CharField(max_length=30,blank=True,null=True)
    Slug=models.SlugField(max_length=100)
    keyword=models.CharField(max_length=50)
    

    def __str__(self):
        return self.Title

class comment(models.Model):
    post=models.ForeignKey(page, on_delete=models.CASCADE,related_name='comment')
    name=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(max_length=80)
    content=models.TextField(max_length=500,blank=True,null=True)
    Created_on=models.DateTimeField(auto_now=False,auto_now_add=True)
    
    def __str__(self):
        return self.name