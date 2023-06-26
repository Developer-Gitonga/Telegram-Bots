from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

TELEGRAM_TOKEN = "6146713943:AAF_7wLdfiv_E-AunQs5MKuKjc-bse0mWZU"

class ChatView(APIView):
    def post(self, request):
        chat_id = request.data.get('chat_id')
        print(f"chat_id: {chat_id}")

        payload = {
            "chat_id": chat_id,
            "text": "Delivery will be made in 2 days"
        }

        try:
            response = requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                json=payload
            )
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            print(f"RESPONSE: {response.content}")

            if response.status_code == 200:
                return Response({'message': 'Message sent successfully'})
            else:
                return Response(
                    {
                        'message': 'Failed to send message',
                        'error_message': response.text,
                    },
                    status=response.status_code
                )
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return Response({'message': 'Failed to send message'}, status=500)


# class TelegramWebhookView(APIView):
#     def post(self, request):
#         body = json.loads(request.body)
#         message = body.get('message')
#         print("Hello world")

#         if message is not None:
#             chat_id = message['chat']['id']
#             text = message.get('text')

#             if text is not None:
#                 reply_message = "Echo: " + text
#                 self.send_reply(chat_id, reply_message)

#         response_body = "Done"
#         return Response(response_body, status=200)

#     def send_reply(self, chat_id, reply_message):
#         url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#         payload = {
#             "chat_id": chat_id,
#             "text": reply_message
#         }

#         try:
#             response = requests.post(url, json=payload)
#             response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             print(f"An error occurred: {e}")
