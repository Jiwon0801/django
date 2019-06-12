from django.contrib import admin
from .models import Movie, Score, Genre
# Register your models here.

admin.site.register(Movie)
admin.site.register(Score)
admin.site.register(Genre)
