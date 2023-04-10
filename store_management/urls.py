
from django.urls import path

from . import views

urlpatterns = [

    path('add_product/', views.add_product, name='add_product'),

    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),

    path('delete_product/<product_slug>/', views.delete_product, name='delete_product'),

    path('<product_id>/add_comment/', views.add_comment, name='add_comment'),

    path('newsletter/', views.newsletter, name='newsletter'),

    path('contact_form/', views.contact_form, name='contact_form'),



]
