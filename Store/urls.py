from django.urls import path
from .views import home, signup, login

urlpatterns = [
    path('', home.Homepage.as_view(), name='home'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login')
]
