from django.contrib import admin
from .models import Post, Style, Purchase, Review

# Register your models here.
admin.site.register(Post)
admin.site.register(Style)
admin.site.register(Purchase)
admin.site.register(Review)