from .models import Profile

def avatar(request):
    context = {}
    if request.user.is_authenticated:
        avatar = Profile.objects.get(user=request.user)
        context["avatar"] = avatar
    return context