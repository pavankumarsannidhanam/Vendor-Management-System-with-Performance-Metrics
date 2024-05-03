from django.urls import path
from vendor_app.views import VendorListCreate, VendorRetrieveUpdateDestroy, PurchaseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy, vendor_performance, acknowledge_purchase_order

urlpatterns = [
    # Vendor API endpoints
    path('api/vendors/', VendorListCreate.as_view()),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroy.as_view()),
    
    # Purchase Order API endpoints
    path('api/purchase_orders/', PurchaseOrderListCreate.as_view()),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view()),
    
    # Vendor Performance Endpoint
    path('api/vendors/<int:vendor_id>/performance/', vendor_performance),
    
    # Update Acknowledgment Endpoint
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order),
]
