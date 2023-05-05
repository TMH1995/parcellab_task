from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from shipping.views import fetchShipmentDetails

fetchShipmentDetailsSwagger = swagger_auto_schema(
    method='post',
    request_body= openapi.Schema(type=openapi.TYPE_OBJECT,
        properties={
            "tracking_number":openapi.Schema(type=openapi.TYPE_STRING, description='Shipment tracking number'),
            "carrier":openapi.Schema(type=openapi.TYPE_STRING, description='Carrier company Ex:(DHL,DPD,GLS)'),
        }),
    responses={200: openapi.Response("retrieve shipment details")}      
)(fetchShipmentDetails)
