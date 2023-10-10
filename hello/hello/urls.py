
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views

admin.site.site_header = "LFC shop admin"
admin.site.site_title = "LFC Admin Portal"
admin.site.index_title = "Welcome to LFC Researcher Portal"

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('api/accounts/',include('accounts.urls')),
]
    