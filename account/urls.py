from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.sing_up, name="sign_up"),
    path("logout/", views.log_out, name="logout"),
    path("profile/view/", views.profile_view, name="profile_view"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    # Favourite
    path("profile/<slug:film>/favourite/add/", views.favourite_add, name="favourite_add"),
    path("profile/favourite/all/", views.favourite_all, name="favourite_all"),

    # Reset Password
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]