from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField(default="")
    
    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('author_detail', args=[str(self.id)])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def articles(self):
        return Hero.objects.filter(author=self)

    @staticmethod
    def get_me(user):
        return Author.objects.get_or_create(user=user)[0]

# Create your models here.
class Hero(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)

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
        
    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])

class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False,
                               related_name='messages_sent')
    recipient = models.ForeignKey(Author, on_delete=models.CASCADE,
                                  related_name='messages_received', default='1')
    title = models.CharField(max_length=100)
    text = models.TextField()

    @property
    def messages(self):
        return Message.objects.filter(author=self.author)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('message_detail', args=[str(self.id)])