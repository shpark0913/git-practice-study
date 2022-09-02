from django.contrib import admin
from .models import Movie
# Register your models here.
# admin.site.register(Article)

class movieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'audience', 
    'release_date', 'genre', 'score','poster_url','description',
    'created_at', 'updated_at')

admin.site.register(Movie,movieAdmin)