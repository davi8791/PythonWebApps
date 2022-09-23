from django.db import models

# Create your models here.
class Hero(models.Model):
    hero_name = models.CharField(max_length=200,default="")
    real_name = models.CharField(max_length=200,default="")
    about_1 = models.TextField(default="")
    about_2 = models.TextField(default="")
    about_source = models.CharField(max_length=500,default="")
    quote = models.TextField(default="")
    primary_rgb = models.CharField(max_length=11,default="")
    strengths = models.CharField(max_length=500,default="")
    weaknesses = models.CharField(max_length=500,default="")
    image = models.CharField(max_length=500,default="")

    def __str__(self):
        return f'{self.hero_name}'