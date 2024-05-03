from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Vendor
from .utils import calculate_on_time_delivery_rate, calculate_quality_rating_avg, calculate_average_response_time, calculate_fulfilment_rate
from django.utils import timezone 

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    performance_metrics = {
        'on_time_delivery_rate': calculate_on_time_delivery_rate(vendor),
        'quality_rating_avg': calculate_quality_rating_avg(vendor),
        'average_response_time': calculate_average_response_time(vendor),
        'fulfilment_rate': calculate_fulfilment_rate(vendor)
    }
    return Response(performance_metrics)

@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    purchase_order = PurchaseOrder.objects.get(pk=po_id)
    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save()
    # Recalculate average_response_time for the vendor
    vendor = purchase_order.vendor
    vendor.average_response_time = calculate_average_response_time(vendor)
    vendor.save()
    return Response({'message': 'Purchase order acknowledged successfully'})

