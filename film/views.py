from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Film, Category, Director
from .forms import WriteReviewForm, SearchForm

# Create your views here.
def home(request):
    films = Film.objects.all()
    paginator = Paginator(films, 1)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    return render(request, "film/home.html", {"page_obj": page_obj})

# -----FILM------
def single(request, film):
    film = get_object_or_404(Film, slug=film)
    return render(request, "film/single.html", {"film": film})

# ------SEARCH FUNCTIONALITY------
def search(request):
    form = SearchForm()
    q = ""
    dropdown_option = ""
    films = []
    categories = []
    directors = []
    if "q" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data["q"]
            dropdown_option = form.cleaned_data["dropdown"]
            if dropdown_option == "film":
                films = Film.objects.filter(title__icontains=q)
            elif dropdown_option == "category":
                categories = Category.objects.filter(name__icontains=q)
            elif dropdown_option == "director":
                directors = Director.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
            else:
                films = Film.objects.filter(title__icontains=q)
                categories = Category.objects.filter(name__icontains=q)
                directors = Director.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
    return render(request, "search/search.html", {"form": form, "q": q, "films": films, "categories": categories, "directors": directors})

# -----CATEGORY-----
def category_all(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 5)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    return render(request, "category/all.html", {"page_obj": page_obj})

def category_single(request, category):
    category = get_object_or_404(Category, slug=category)
    films = Film.objects.filter(category=category)
    return render(request, "category/single.html", {"category": category, "films": films})

# -----DIRECTOR-----
def director_single(request, director):
    director = get_object_or_404(Director, slug=director)
    return render(request, "director/single.html", {"director": director})

# ----REVIEWS-----
def review_all(request, film):
    film = get_object_or_404(Film, slug=film)
    return render(request, "film/review/review_all.html", {"film": film})

@login_required
def review_write(request, film):
    film = get_object_or_404(Film, slug=film)
    if request.method == "POST":
        review_form = WriteReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.film = film
            review.save()
            return redirect("film:single", film=film.slug)
    else:
        review_form = WriteReviewForm()
    return render(request, "film/review/review_write.html", {"film": film, "review_form": review_form})