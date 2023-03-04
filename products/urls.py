
from django.urls import path
from . import views

urlpatterns = [

    path('', views.all_products, name='products'),

    path('<product_slug>/', views.product_detail, name='product_detail'),

    path('category/<category_slug>/', views.search_category, name='search_category'),

]
