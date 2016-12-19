from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(default=0)
    poster_src = models.CharField(max_length=100)
    release_date = models.DateField('date release')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

