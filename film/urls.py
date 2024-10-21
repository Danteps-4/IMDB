from django.urls import path
from . import views

app_name = "film"

urlpatterns = [
    path("", views.home, name="home"),
    path("film/<slug:film>/", views.single, name="single"),
    # Search
    path("search/", views.search, name="search"),
    # Category
    path("category/all/", views.category_all, name="category_all"),
    path("category/<slug:category>/", views.category_single, name="category_single"),
    # Director
    path("director/<slug:director>/", views.director_single, name="director_single"),
    # Review
    path("review/all/<slug:film>/", views.review_all, name="review_all"),
    path("review/write/<slug:film>/", views.review_write, name="review_write"),
]