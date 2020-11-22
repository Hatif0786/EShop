from django.shortcuts import render, redirect
from Store.models.product import Product
from Store.models.category import Category
from django.views import View

class Homepage(View):
    def get(self, request):
        prdcts = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            prdcts = Product.get_all_products_by_category(categoryID)
        else:
            prdcts = Product.get_all_products()
        #print("You are :", request.session.get('email'))
        return render(request, "homepage.html", {"HProducts": prdcts, "Categories": categories})


    def post(self, request):
        productID = request.POST.get('productID')
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(productID)
            if quantity:
                 cart[productID] = quantity + 1
            else:
                cart[productID] = 1
        else:
            cart = {}
            cart[productID] = 1

        request.session['cart'] = cart
        print(cart)
        return redirect('home')




