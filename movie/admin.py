from django.contrib import admin

from .models import Movie, Comment, Actor

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Actor)

# Register your models here.
