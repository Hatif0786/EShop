from django.shortcuts import render
from .models.product import Product

# Create your views here.
def homepage(request):
    prdcts = Product.get_all_products()
    return render(request, "homepage.html", {'HProducts': prdcts})