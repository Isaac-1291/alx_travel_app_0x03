from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'destination', 'check_in', 'check_out', 'created_at']
        read_only_fields = ['user', 'created_at']