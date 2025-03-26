from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Item, Order, Notification

channel_layer = get_channel_layer()

def broadcast(message):
    async_to_sync(channel_layer.group_send)(
        "notifications", {"type": "send_notification", "message": message}
    )

@receiver(post_save, sender=Item)
def handle_item_save(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    message = f"Item '{instance.name}' {action}."
    Notification.objects.create(message=message)
    broadcast(message)

@receiver(post_delete, sender=Item)
def handle_item_delete(sender, instance, **kwargs):
    message = f"Item '{instance.name}' deleted."
    Notification.objects.create(message=message)
    broadcast(message)

@receiver(post_save, sender=Order)
def handle_order_save(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    message = f"Order for item '{instance.item.name}' {action}."
    Notification.objects.create(message=message)
    broadcast(message)

@receiver(post_delete, sender=Order)
def handle_order_delete(sender, instance, **kwargs):
    message = f"Order for item '{instance.item.name}' deleted."
    Notification.objects.create(message=message)
    broadcast(message)
