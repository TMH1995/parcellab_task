from django.urls import path,include
from shipping.views import fetchShipmentDetails
from shipping.swagger import *

apis = [
    path('fetchShipment',fetchShipmentDetails,name='fetchShipmentDetails')
]

urlpatterns = [
    path('shipments/', include(apis)),
]