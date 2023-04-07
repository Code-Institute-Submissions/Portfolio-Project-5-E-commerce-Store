
from django.urls import path

from . import views

urlpatterns = [

    path('', views.all_products, name='products'),

    path('<int:product_slug>/', views.product_detail, name='product_detail'),

    path('add_product/', views.add_product, name='add_product'),

    path('category/<category_slug>/', views.search_category, name='search_category'),

]
