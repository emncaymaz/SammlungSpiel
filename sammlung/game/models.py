from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Game(models.Model):
    AGE =[
            ('1-3','1-3'),
            ('4-7','4-7'),
            ('8-10','8-10'),
            ('10+','10+'),
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Spielname')
    age  =models.CharField(choices=AGE,default='1-3', max_length=20, verbose_name='Geeignet für alter', blank=True, null=True)
    instructions = models.TextField(verbose_name='Anleitung', blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name


class Review(models.Model):
    RATING = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=240, blank=True, null=True, verbose_name='Kommentar')
    rating = models.IntegerField(choices=RATING, blank=True, null=True, verbose_name='Sterne')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review