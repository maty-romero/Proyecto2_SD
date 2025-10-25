# Raw Telemetry Suscriber 
"""
1. Suscripcion a Topico telemetria datos crudos
2. Formateo de datos 
3. Guardado en BD - Colecciones por Parques/Wind_Farms 
"""
import json

from Shared.GenericMQTTClient import GenericMQTTClient


# TOPIC_TELEMETRY = "farms/{farm_id}/turbines/+/raw_telemetry"

class RawTelemtrySuscriber:
    def __init__(self, farm_id: int):
        self.RAW_TELEMETRY_TOPIC = "ds"
        self.raw_telemetry_topic = f"farms/{farm_id}/turbines/+/raw_telemetry" # suscription topic 
        self.mqtt_client = GenericMQTTClient(client_id="stat-processor") 
        # Resto de la configuracion
        
    def start(self):
        self.mqtt_client.connect()
        self.mqtt_client.subscribe(self.raw_telemetry_topic, self._message_callback)
        import time
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.mqtt_client.disconnect()
    
    
    def _message_callback(self, client, userdata, msg):
        payload = msg.payload.decode()
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            data = payload
        print(f"\nRecibido en '{msg.topic}': {data} \n******")
        
if __name__ == '__main__':
    sub = RawTelemtrySuscriber(farm_id=1)
    sub.start()
    