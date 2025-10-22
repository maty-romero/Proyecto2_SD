#### Backend Alertas / Historial

__Responsabilidades__
1. Publicacion de alertas 
    - Clima 
    - Turbinas en general (ej: posible falla / mantenimiento requerido T-028) 
2. Suscripcion de topico telemetria → Guardado de historial en BD (MongoDB)


__Endpoints__ 
(Broker EQMX o DashBoard como clientes)
- [POST] /farm/{id_farm}/turbines/telemetry 
    - body: datos json
- [GET] /farm/{id_farm}/history/filter=from_date_to...
 

