from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import TruckSerializer, ArrivalSerializer, DeportSerializer
from tracker.models import Truck, Arrival, Deport

@api_view(['GET'])
def receive(request):
    data = request.data
    try:
        truck = Truck.objects.get(token=data.get('token', default=None))
    except Truck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # data  = {'truck':truck}
    if truck.at_poligon:
        event = Deport.objects.create(truck=truck)
        truck.at_poligon = False
        truck.save()
        # serializer = DeportSerializer(data=data)
    else:
        event = Arrival.objects.create(truck=truck)
        truck.at_poligon = True
        truck.save()
        # serializer = ArrivalSerializer(data=data)

    print ' # Event created: ' + str(event.time)
    return Response(status=status.HTTP_201_CREATED)
