from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(default=0)
    poster_src = models.CharField(max_length=100, blank=True, default='')
    release_date = models.DateField('date release')
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text_1 = models.CharField(max_length=200)
    text_2 = models.CharField(max_length=200)
    text_3 = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)

