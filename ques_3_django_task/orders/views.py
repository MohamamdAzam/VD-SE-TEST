from .models import Order
from django.shortcuts import render, redirect
from .forms import OrderForm

def top_customers_view(request):
    top_customers = Order.get_top_customers()
    return render(request, 'orders/top_customers.html', {'top_customers': top_customers})


def add_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('top_customers') 
    else:
        form = OrderForm()
    return render(request, 'orders/add_order.html', {'form': form})
