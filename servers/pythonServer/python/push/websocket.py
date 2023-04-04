import json
from channels.generic.websocket import AsyncWebsocketConsumer

# receive message and send it back to client
class WebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('websocket consumer connected')
        await self.accept()

    async def disconnect(self, close_code):
        print("disconnect")
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("receiving message from client", message)

        await self.send(text_data=json.dumps({'message': message + "wow",}))