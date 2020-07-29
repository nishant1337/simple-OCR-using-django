from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.home,name='home'), 
    path('convert',views.convert,name='convert'), 
]