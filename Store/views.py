from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from django.http import HttpResponse
from .models.customer import Customer

# Create your views here.
def homepage(request):
       prdcts = None
       categories = Category.get_all_categories()
       categoryID = request.GET.get('category')
       if categoryID:
          prdcts = Product.get_all_products_by_category(categoryID)
       else:
          prdcts = Product.get_all_products()
       return render(request, "homepage.html", {"HProducts": prdcts, "Categories": categories})


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        Post_Data = request.POST
        first_Name = Post_Data.get("first name")
        last_Name = Post_Data.get("lastname")
        phone = Post_Data.get("phone")
        email = Post_Data.get("email")
        password = Post_Data.get("password")
        customer = Customer(firstName=first_Name,
                            lastName=last_Name,
                            phone=phone,
                            email=email,
                            password=password)
        value = {"firstName": first_Name,
                 "lastName": last_Name,
                 "phone": phone,
                 "email": email}

        #validation of enteries
        err_message = None
        if not first_Name:
            err_message = "First Name is required"
        elif len(first_Name) < 4:
            err_message = "First Name should be more than 4 character's."
        elif not last_Name:
            err_message = "Last Name is required"
        elif len(last_Name) < 4:
            err_message = "Last Name should be more than 4 character's."
        elif not phone:
            err_message = "Phone is mandatory!"
        elif len(phone) < 10:
            err_message = "Phone No. should'nt be less than 10 digits ."
        elif not password:
            err_message = "Password must be entered"
        elif len(password) < 8:
            err_message = "Password should be 8 character's long and must be alphanumeric."
        elif customer.isExists():
            err_message = "Email already Exists"


        #saving of the enteries
        if not err_message:
            customer.save()
            print(first_Name, last_Name, phone, email, password)
            return redirect('home')
        else:

            return render(request, "signup.html", {"error": err_message, "values": value})