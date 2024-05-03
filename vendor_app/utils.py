from django.utils import timezone
from .models import Vendor, PurchaseOrder
from .models import models
def calculate_on_time_delivery_rate(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_pos = completed_pos.filter(delivery_date__lte=timezone.now())
    return (on_time_pos.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

def calculate_quality_rating_avg(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    return completed_pos.aggregate(avg_quality_rating=models.Avg('quality_rating'))['avg_quality_rating'] or 0


def calculate_average_response_time(vendor):
    acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = [(po.acknowledgment_date - po.issue_date).seconds / 60 for po in acknowledged_pos]
    return sum(response_times) / len(response_times) if len(response_times) > 0 else 0

def calculate_fulfilment_rate(vendor):
    total_pos = PurchaseOrder.objects.filter(vendor=vendor)
    fulfilled_pos = total_pos.filter(status='completed')
    return (fulfilled_pos.count() / total_pos.count()) * 100 if total_pos.count() > 0 else 0
