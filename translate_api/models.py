from django.db import models

# Create your models here.

class ParentCategory(models.Model):
    """
    class to create model for storing parent category
    """
    title= models.CharField(max_length=255, blank=False, null=False)
    thumbnail_img = models.URLField(max_length=500, null=False, blank=True)