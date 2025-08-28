# listings/views.py
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user)
        
        # Trigger the email task asynchronously
        send_booking_email.delay(
            self.request.user.email,
            f"Booking ID: {booking.id}, Destination: {booking.destination}"
        )