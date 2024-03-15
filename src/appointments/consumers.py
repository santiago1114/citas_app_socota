import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class TurnoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
        self.group_name = 'turno_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
            )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        
    def send_turno(self, data):
        self.send(text_data=json.dumps({
            'type': 'turno',
            'id': data['instance'].id,
            'enEspera': data['instance'].en_espera,
            'nombres': data['instance'].cita.paciente.nombres,
            'apellidos': data['instance'].cita.paciente.apellidos,
        }))
