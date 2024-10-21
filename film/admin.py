from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name", )}

@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age"]
    prepopulated_fields = {"slug": ("first_name", "last_name")}

@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(models.Review)