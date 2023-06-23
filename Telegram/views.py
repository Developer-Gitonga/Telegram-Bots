from django.shortcuts import render
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.http import HttpResponse

TELEGRAM_TOKEN = settings.TELEGRAM_BOT_TOKEN
VERIFY_TOKEN = settings.TELEGRAM_VERIFY_TOKEN

# Create your views here.
class ChatView(APIView):
    '''
    Logic to handle Telegram chats
    '''
    def post(self, request):
        """
        Send a text message.
        """
        # Retrieve the chat ID from the request
        # message = request.data.get('message')
        chat_id = request.data.get('chat_id')

        # Create the payload for the Telegram Bot API request
        payload = {
            "chat_id":chat_id,
            "text":"Hello, World!"
        }

        # Make the POST request to the Telegram Bot API
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        )

        # Check the response status and handle accordingly
        if response.status_code == 200:
            # Message sent successfully
            return Response({'message': 'Message sent successfully'})
        else:
            # Error occurred while sending the message
            return Response(
                {
                    'message': 'Failed to send message',
                    'error_message': response.text,
                }, status=response.status_code)


class TelegramWebhookView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        message = body.get('message')

        if message is not None:
            chat_id = message['chat']['id']
            text = message.get('text')

            if text is not None:
                reply_message = "Echo: " + text
                self.send_reply(chat_id, reply_message)

        response_body = "Done"
        return HttpResponse(json.dumps(response_body), status=200)

    def send_reply(self, chat_id, reply_message):
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": reply_message
        }

        response = requests.post(url, json=payload)
        response.raise_for_status()
