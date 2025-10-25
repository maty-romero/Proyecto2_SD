"""
1. Extraccion datos telemetria cada cierto intervalo tiempo - 10/15 seg (N parques eolicos) 
2. Calculo de estadisticas
3. Publicar estadisticas en topico: farms/{farm_id}/proc_telemetry - que consume o suscribe dashboard
"""