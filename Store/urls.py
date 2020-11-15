
from django.urls import path
from .views import homepage, signup

urlpatterns = [
    path('', homepage),
    path('signup', signup),
]
