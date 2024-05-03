"""
URL configuration for vendor_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.urls import path, include
from vendor_app.views import VendorListCreate, VendorRetrieveUpdateDestroy, PurchaseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy,vendor_performance,acknowledge_purchase_order
urlpatterns = [
    path('api/vendors/', VendorListCreate.as_view()),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroy.as_view()),
    path('api/purchase_orders/', PurchaseOrderListCreate.as_view()),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view()),
    path('api/vendors/<int:vendor_id>/performance/', vendor_performance),
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order),
]
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('vendor_app.urls')),  # Include app-level URLs
# ]


