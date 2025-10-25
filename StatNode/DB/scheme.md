### Colecciones a considerar dentro del esquema BD 
- BD contiene -> Colecciones (Telemtry, Alerts, etc) -> Documentos { } 

- Colección 
    - Es como la tabla en SQL, el contenedor donde se agrupan los documentos. 
    - Es el punto de partida cuando querés buscar datos.

- Documento 
    - Es como una fila en SQL
    - En MongoDB es básicamente un diccionario/JSON ({...}) que contiene los campos con sus valores.

### Colecciones 
1. Telemetry
2. Alerts
3. Users (Del frontend o por fuera del broker)
4. Maintance - opcional (Req. Futuro)

*** 
A modo de referencia
~~~
Telemetry
{
  "_id": ObjectId("6567b8a9c0f4a12d34567890"),
  "farm_id": "F-001",
  "turbine_id": "T-001",
  "timestamp": ISODate("2025-10-25T08:30:00Z"),
  "wind_speed_mps": 12.5,
  "wind_direction_deg": 270,
  "rotor_speed_rpm": 15.2,
  "blade_pitch_angle_deg": 5,
  "gearbox_temperature_c": 65,
  "output_voltage_v": 400,
  "generated_current_a": 300,
  "operational_state": "active"
}

Alerts
{
  "_id": ObjectId("6567b9b1c0f4a12d34567891"),
  "farm_id": "F-001",
  "turbine_id": "T-003",
  "timestamp": ISODate("2025-10-25T09:15:00Z"),
  "alert_type": "overheat",
  "message": "Gearbox temperature exceeds threshold",
  "severity": "high",
  "acknowledged": false
}

Users
{
  "_id": ObjectId("6567ba2ac0f4a12d34567892"),
  "user_id": "U-001",
  "name": "Juan Perez",
  "email": "juan@example.com",
  "role": "viewer",
  "api_key": "abcd1234"
}
~~~

