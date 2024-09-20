from django.urls import path
from .views import top_customers_view, add_order_view

urlpatterns = [
    path('top-customers/', top_customers_view, name='top_customers'),
    path('add-order/', add_order_view, name='add_order'),
]

