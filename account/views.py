from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, EditProfileForm, UserProfileForm
from django.contrib.auth import login, logout, authenticate
from film.models import Film
from .models import Profile

# Create your views here.

# -----LOGIN SIGN UP LOGOUT-----
def sing_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("film:home")
    else:
        form = RegistrationForm()
    return render(request, "registration/sign_up.html", {"form": form})

def log_out(request):
    logout(request)
    return redirect("login")


# -----PROFILE-----
@login_required
def profile_view(request):
    return render(request, "profile/view.html")

@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = EditProfileForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("account:profile_view")
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, "profile/edit.html", {"user_form": user_form, "profile_form": profile_form})


# -----FAVOURITE-----
@login_required
def favourite_add(request, film):
    film = get_object_or_404(Film, slug=film)

    if film in request.user.favourites.all():
        request.user.favourites.remove(film)
    else:
        request.user.favourites.add(film)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def favourite_all(request):
    favourites = request.user.favourites.all()
    return render(request, "profile/favourites/all.html", {"favourites": favourites})