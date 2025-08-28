from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_email(user_email, booking_details):
    subject = "Booking Confirmation"
    message = f"Hello, your booking has been confirmed.\nDetails: {booking_details}"
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'no-reply@travelapp.com')
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)