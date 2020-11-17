from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from django.http import HttpResponse
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password


def validateCustomer(customer):
    err_message = None
    if not customer.firstName:
        err_message = "First Name is required"
    elif len(customer.firstName) < 4:
        err_message = "First Name should be more than 4 character's."
    elif not customer.lastName:
        err_message = "Last Name is required"
    elif len(customer.lastName) < 4:
        err_message = "Last Name should be more than 4 character's."
    elif not customer.phone:
        err_message = "Phone is mandatory!"
    elif len(customer.phone) < 10:
        err_message = "Phone No. should'nt be less than 10 digits ."
    elif not customer.password:
        err_message = "Password must be entered"
    elif len(customer.password) < 8:
        err_message = "Password should be 8 character's long and must be alphanumeric."
    elif customer.isExists():
        err_message = "Email already Exists"
    return err_message


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
       return registerUser(request)


def registerUser(request):
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

        error = validateCustomer(customer)
        if not error:
            customer.password = make_password(customer.password)
            customer.save()
            print(first_Name, last_Name, phone, email, password)
            return redirect('home')
        else:
            return render(request, "signup.html", {"error": error, "values": value})


def logIn(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        passwrd = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(passwrd, customer.password)
            if flag:
                return redirect('home')
            else:
                error_message = "Email or Password invalid!!"
        else:
            error_message = "Email or Password invalid!!"
    print(email, passwrd)
    return render(request, 'login.html', {'error': error_message})

