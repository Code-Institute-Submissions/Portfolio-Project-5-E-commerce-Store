
from django.urls import path

from . import views

urlpatterns = [

    path('add_product/', views.add_product, name='add_product'),

    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),

    path('view_comments/', views.view_comments, name='view_comments'),

    path('approve_comment/<int:comment_id>', views.approve_comment, name='approve_comment'),

    path('delete_comment/<comment_id>/', views.delete_comment, name='delete_comment'),

    path('delete_product/<product_slug>/', views.delete_product, name='delete_product'),

    path('<product_id>/add_comment/', views.add_comment, name='add_comment'),

    path('newsletter/', views.newsletter, name='newsletter'),

    path('view_newsletter/', views.view_newsletter, name='view_newsletter'),

    path('delete_subscriber/<email_id>/', views.delete_subscriber, name='delete_subscriber'),

    path('contact_form/', views.contact_form, name='contact_form'),

    path('store_inbox/', views.store_inbox, name='store_inbox'),

    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),

]
