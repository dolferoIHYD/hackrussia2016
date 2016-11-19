from rest_framework import serializers

from tracker.models import Truck, Arrival, Deport

class TruckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck
        fields = ('token', 'at_poligon', )


class ArrivalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arrival
        fields = ('time', 'truck')


class DeportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deport
        fields = ('time', 'truck')
