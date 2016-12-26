from django.contrib import admin

from .models import Kind, Item, Review
# Register your models here.

admin.site.register(Kind)
admin.site.register(Item)
admin.site.register(Review)

