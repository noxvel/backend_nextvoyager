from django.db import models

# Create your models here.

class Kind(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name 

class Item(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(default=0)
    poster_src = models.ImageField(upload_to='items_poster/', blank=True, default='')
    release_date = models.DateField('date release')
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text_1 = models.CharField(max_length=200)
    text_2 = models.CharField(max_length=200)
    text_3 = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

