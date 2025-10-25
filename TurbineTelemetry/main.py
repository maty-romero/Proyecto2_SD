import time

from TurbineTelemetry.WindTurbine import WindTurbine

if __name__ == "__main__":
    # -- Turbinas simuluacion 
    turbine1 = WindTurbine(farm_id=1, turbine_id=1)
    turbine2 = WindTurbine(farm_id=1, turbine_id=2)
    turbine3 = WindTurbine(farm_id=1, turbine_id=3)
    # arranque turbina (conexion mqtt y envio de telemetria)
    turbine1.start() 
    turbine2.start()
    turbine3.start()
    print("Simulador corriendo. Presiona Ctrl+C para detener.")
    
    try:
        # Mantener el hilo principal vivo mientras la turbina publica
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo turbina...")
        turbine1.stop()
        print("Turbina detenida. Saliendo.")