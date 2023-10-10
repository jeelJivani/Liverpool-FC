from django.contrib import admin
from django.urls import path
from .views import *
from . import views     
from  django.contrib.auth.decorators import login_required

urlpatterns = [
    path('products',login_required(ProductView.as_view()),name="products"),
] 