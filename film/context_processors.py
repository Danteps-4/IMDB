from .models import Category

def categories(request):
    categories_all = Category.objects.all()
    return {"categories": categories_all}