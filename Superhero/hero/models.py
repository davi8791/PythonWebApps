from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Investigator(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField(default="")
    
    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('investigator_detail', args=[str(self.id)])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def articles(self):
        return Hero.objects.filter(investigator=self)

    @staticmethod
    def get_me(user):
        return Investigator.objects.get_or_create(user=user)[0]

def get_upload(instance, filename):
    # if instance.folder:
    #     return f'images/{instance.folder}/{filename}'
    return f'images/{filename}'

# Create your models here.
class Hero(models.Model):
    investigator = models.ForeignKey(Investigator, on_delete=models.CASCADE, editable=False)

    hero_name = models.CharField(max_length=200,default="")
    real_name = models.CharField(max_length=200,default="")
    about_1 = models.TextField(default="")
    about_2 = models.TextField(default="")
    about_source = models.CharField(max_length=500,default="")
    quote = models.TextField(default="")
    primary_rgb = models.CharField(max_length=11,default="")
    strengths = models.CharField(max_length=500,default="")
    weaknesses = models.CharField(max_length=500,default="")
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)

    def __str__(self):
        return f'{self.hero_name}'
        
    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])