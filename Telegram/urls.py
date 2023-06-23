from django.urls import path
from .views import ChatView, TelegramWebhookView

urlpatterns = [
    # Endpoint for sending a message via Telegram
    path('telegram/send-message/', ChatView.as_view(), name='telegram-send-message'),

    # Endpoint for receiving messages from Telegram
    path('telegram/webhook/', TelegramWebhookView.as_view(), name='telegram-webhook')
]