from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    
class ImageType(models.Model): 
    ImageTypeName = models.CharField(max_length=200, null=True) 
    ImageTypeDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f"{self.id}. {self.ImageTypeName}"


class Image(models.Model): 
    ImageName = models.CharField(max_length=200, null=True) 
    ImageURL = models.ImageField(upload_to='images/',null=True,blank=True) 
    ImageLink = models.CharField(max_length=200, null=True) 
    ImageTypeID = models.ForeignKey(ImageType, on_delete=models.CASCADE, null=True) 
    Active = models.CharField(max_length=200, null=True) 
    ImageDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f'{self.id} {self.ImageName}'
    
class Menu(models.Model):
    MenuNameKH = models.CharField(max_length=200, null=True)
    MenuNameEN = models.CharField(max_length=200, null=True)
    OrderBy = models.IntegerField(blank=True,null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f'{self.id} | {self.MenuNameKH} | {self.MenuNameEN} | {self.CreatedDate}'
    

class MenuDetail(models.Model):
    MenuID = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    Description =  RichTextUploadingField(null=True)
    MenuDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    def __str__(self):         
        return self.MenuID.MenuNameEN