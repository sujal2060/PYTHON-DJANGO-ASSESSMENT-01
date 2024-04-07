from django.urls import path
from .views import homeview,aboutview,contactview,loginview,registerview #imported

app_name = 'appassessment'   #add your app_name here

urlpatterns = [
    path('', homeview, name='home-response'),
    path('/about', aboutview, name='about-response'),
    path('/contact', contactview, name='contact-response'),
    path('/login', loginview, name='login-response'),
    path('/register', registerview, name='register-response'),
]
