from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


def user_directory_path(instance, filename):
    return f"films/{instance.id}/{filename}"

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    @property
    def total_films(self):
        return self.film_set.count()

    def __str__(self):
        return self.name
    
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    city_of_birth = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, blank=True)

    @property
    def total_films(self):
        return self.film_set.count()
    
    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Film(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=300)
    description = models.TextField()
    duration = models.IntegerField() # Duration in minutes
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.ManyToManyField(Category,blank=True)
    director = models.ManyToManyField(Director, blank=True)
    release_date = models.DateTimeField()
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, null=True)
    image = models.ImageField(upload_to=user_directory_path, default="films/default.jpg")
    favourites = models.ManyToManyField(User, related_name="favourites", blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_reviews(self):
        return self.reviews.count()

    def __str__(self):
        return self.title
    
class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("publish", )

    def __str__(self):
        return f"Review: {self.film.title} by {self.user.username}"