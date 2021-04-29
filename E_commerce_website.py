urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discription = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
    from django.contrib import admin
from .models import *


admin.site.register(Product)
from django.shortcuts import render
from .models import *

def products(request):
    productss = Product.objects.all()
    return render(request, 'products.html', {'productss':productss})
from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.products, name='products'),

]{% for product in productss %}
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="{{ product.image }}" alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">{{ product.productname }}</h5>
    <p class="card-text">{{ product.discription }}</p>
    <p class="card-text">Price - {{ product.price }}</p>
    <a href="#" class="btn btn-primary">Buy Now</a>
  </div>
</div>
{% endfor %}
django-admin createsuperuser
python manage.py runserver
