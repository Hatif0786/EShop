
from django.urls import path
from .views import homepage, signup

urlpatterns = [
    path('', homepage, name='home'),
    path('signup', signup),
]
