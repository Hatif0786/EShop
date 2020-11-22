from django.views import View
from django.shortcuts import redirect, render
from Store.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
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

        error = self.validateCustomer(customer)
        if not error:
            customer.password = make_password(customer.password)
            customer.save()
            print(first_Name, last_Name, phone, email, password)
            return redirect('home')
        else:
            return render(request, "signup.html", {"error": error, "values": value})

    def validateCustomer(self, customer):
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
