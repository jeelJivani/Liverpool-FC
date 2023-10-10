from django.shortcuts import render,redirect
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

from django.db.models import Q




# Create your views here.



class ProductView(APIView):
    
    def get(self, request):
        # Get query parameters
        category = self.request.query_params.get('category')
        search_query = self.request.query_params.get('search')
        size = self.request.query_params.get('size')

        # Start with all products
        queryset = Product.objects.all()

        # Filter by category if provided
        if category:
            queryset = queryset.filter(category__category_name=category)
        if size:
            queryset = queryset.filter(size__size=size)

        # Filter by search query if provided
        if search_query:
            queryset = queryset.filter(
                Q(product_name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(price__icontains=search_query)|
                Q(category__category_name= search_query)
            )

        return render(request, 'products/Shop_product_list.html', {'products': queryset})
