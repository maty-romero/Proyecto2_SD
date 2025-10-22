import random
import threading
import time

from GenericMQTTClient import GenericMQTTClient

TOPIC_TELEMETRY = "farm/turbine/telemetry"
TOPIC_STATUS = "farm/turbine/status"
# TOPIC_ALERTS = "farm/turbine/alerts"  topico del backend history/alerts

class WindTurbine:
    def __init__(self, turbine_id: str):
        self.turbine_id = turbine_id
        self.telemetry_topic = TOPIC_TELEMETRY
        # self.status_topic = TOPIC_STATUS
        
        # cliente mqtt con id unico
        self.mqtt_client = GenericMQTTClient(client_id=self.turbine_id) # T-001, T-002, etc 
        self.publish_interval = 15 # segundos
        self._stop_event = threading.Event()
        self._thread = None

    def get_telemetry_data(self) -> dict:
        # Genera datos de turbina 
        return {
            "turbine_id": self.turbine_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "wind_speed_mps": round(random.uniform(3.0, 25.0), 2),
            "wind_direction_deg": random.randint(0, 360),
            "atmospheric_pressure_hpa": round(random.uniform(980, 1030), 1),
            "rotor_speed_rpm": round(random.uniform(10, 20), 2),
            "blade_pitch_angle_deg": round(random.uniform(0, 30), 1),
            "gearbox_temperature_c": round(random.uniform(40, 90), 1),
            "output_voltage_v": round(random.uniform(380, 420), 1),
            "generated_current_a": round(random.uniform(200, 500), 1),
            "operational_state": "active" # por ahora siempre activo
            #"operational_state": random.choice(["active", "stopped", "fault", "maintenance"])
        }

    def start(self):
        """
        1. Configuracion LWT 
        2. Conecta del mqqt client 
        3. loop envio de telemetría 
        """
        # En caso de caida de la turbina
        lwt_payload = {"turbine_id": self.turbine_id, "state": "offline"}
        self.mqtt_client.set_lwt(TOPIC_STATUS, lwt_payload, qos=1, retain=True)

        self.mqtt_client.connect()
       
        # arrancar hilo que publica telemetría
        if self._thread is None or not self._thread.is_alive():
            self._stop_event.clear()
            self._thread = threading.Thread(target=self._send_telemetry, daemon=True)
            self._thread.start()

    def _send_telemetry(self):
        while not self._stop_event.is_set():
            data: dict = self.get_telemetry_data()
            # el payload lo crea la entidad; el cliente solo publica en el topic que se le pasa
            # conversion data a JSON lo hace mqtt_client 
            self.mqtt_client.publish(TOPIC_TELEMETRY, data, qos=0, retain=False)
            self._stop_event.wait(self.publish_interval)

    def stop(self):
        """Detiene el hilo, limpia retained status y desconecta (todo desde la entidad)."""
        self._stop_event.set()
        if self._thread:
            self._thread.join()
        # limpiar retained status 
        self.mqtt_client.clear_retained(TOPIC_STATUS)
        self.mqtt_client.disconnect()