import time
import queue
from django.http import StreamingHttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Item, Order, Notification
from .serializers import ItemSerializer, OrderSerializer
from .util import sse_event_queue

def event_stream():

    while True:
        try:
            message = sse_event_queue.get(timeout=10)
            yield f"data: {message}\n\n"
        except queue.Empty:
            yield ": keep-alive\n\n"

@api_view(['GET'])
def sse_notifications(request):

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response

@api_view(['POST'])
def mark_notifications_read(request):

    Notification.objects.filter(read=False).update(read=True)
    return Response({"status": "All notifications marked as read."})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
