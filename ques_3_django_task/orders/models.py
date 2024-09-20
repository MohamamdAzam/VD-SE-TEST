from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

    @classmethod
    def get_top_customers(cls):
        six_months_ago = timezone.now() - timedelta(days=180)
        return (
            cls.objects.filter(order_date__gte=six_months_ago)
            .values('customer')
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )
