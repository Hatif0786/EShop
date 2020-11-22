from django.views import View
from Store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        passwrd = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(passwrd, customer.password)
            if flag:
                request.session['customerID'] = customer.id
                request.session['email'] = customer.email
                return redirect('home')
            else:
                error_message = "Email or Password invalid!!"
        else:
            error_message = "Email or Password invalid!!"

        print(email, passwrd)
        return render(request, 'login.html', {'error': error_message})
