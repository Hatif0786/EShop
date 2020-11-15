from django.shortcuts import render
from .models.product import Product
from .models.category import Category

# Create your views here.
def homepage(request):
       prdcts = None
       categories = Category.get_all_categories()
       categoryID = request.GET.get('category')
       if categoryID:
          prdcts = Product.get_all_products_by_category(categoryID);
       else:
          prdcts = Product.get_all_products();
       return render(request, "homepage.html", {"HProducts": prdcts, "Categories": categories})


def signup(request):
    return render(request, 'signup.html')