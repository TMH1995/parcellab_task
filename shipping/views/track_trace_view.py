from django.http import JsonResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework import status
from shipping.serializers import ShipmentSerializer
from shipping.models import Shipment


@api_view(['POST', ])
def fetchShipmentDetails(request: HttpRequest) -> JsonResponse:
    try:
        tracking_number= request.data.get('tracking_number',None)
        carrier= request.data.get('carrier',None)
        shipment=Shipment.objects.get(carrier=carrier,tracking_number=tracking_number)
        shipmentSerializer=ShipmentSerializer(instance=shipment)
        return JsonResponse({'data': shipmentSerializer.data}, status=status.HTTP_200_OK) 

    except Shipment.DoesNotExist:
        return JsonResponse({'message': 'Wrong tracking number or carrier'}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
