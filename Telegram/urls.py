from django.urls import path
from .views import ChatView

urlpatterns = [
    # Endpoint for sending a message via Telegram
    path('telegram/send-message/', ChatView.as_view(), name='telegram-send-message'),

]