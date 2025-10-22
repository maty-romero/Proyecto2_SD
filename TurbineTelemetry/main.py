import time
from WindTurbine import WindTurbine

if __name__ == "__main__":
    # -- Turbinas simuluacion 
    turbine1 = WindTurbine("T-001")
    turbine1.start() # arranque turbina (conexion mqtt y envio de telemetria)
    
    print("Simulador corriendo. Presiona Ctrl+C para detener.")
    
    try:
        # Mantener el hilo principal vivo mientras la turbina publica
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo turbina...")
        turbine1.stop()
        print("Turbina detenida. Saliendo.")