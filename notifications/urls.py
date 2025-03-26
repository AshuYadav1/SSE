from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ItemViewSet, OrderViewSet,
    sse_notifications, mark_notifications_read
)

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sse/', sse_notifications, name='sse_notifications'),
    path('notifications/mark-read/', mark_notifications_read, name='mark_notifications_read'),
]
