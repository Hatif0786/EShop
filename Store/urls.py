
from django.urls import path
from .views import homepage, signup, logIn

urlpatterns = [
    path('', homepage, name='home'),
    path('signup', signup),
    path('login', logIn)
]
