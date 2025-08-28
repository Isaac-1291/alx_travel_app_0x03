# alx_travel_app_0x03

## Background Task with Celery

- Celery is configured with RabbitMQ as the broker.
- Booking confirmation emails are sent asynchronously.
- To run Celery worker:

  celery -A alx_travel_app worker --loglevel=info
