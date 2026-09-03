import json
import time
import random
import hashlib
from datetime import datetime
from typing import Dict, Any

def generar_evento():
    """
    Simula la generacion de eventos de telemetria desde un nodo Edge IoT

    Distribucion de eventos:
    - 70% trafico normal
    - 20% Anomalia leve (temperatura alta o latencia)
    - 10% evento critico (Intento de acceso no autorizado) 

    return: 
        dict: Un diccionario con los datos del evento timestamp y hash de integridad    
    """
    prob = random.random()
    
    if prob < 0.70:
        tipo_evento = "trafico_normal"
        severidad = random.randint(1, 2) 
        payload = {"status": "ok", "cpu_temp": round(random.uniform(40.0, 55.0), 2)}
    elif prob < 0.90:
        tipo_evento = "anomalia_leve"
        severidad = random.randint(3, 4)
        payload = {"status": "warning", "cpu_temp": round(random.uniform(75.0, 85.0), 2), "error": "latencia_alta"}
    else:
        tipo_evento = "evento_critico"
        severidad = 5 
        payload = {"status": "critical", "alerta": "intento_acceso_reiterado", "origen": "ip_desconocida"}

    evento = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "nodo_id": f"Nodo-IoT-{random.randint(1, 3)}",
        "tipo_evento": tipo_evento,
        "severidad": severidad,
        "payload": payload
    }

    # Generación del hash de integridad (SHA-256) para validacion en destino
    evento_string = json.dumps(evento, sort_keys=True)
    evento["hash_integridad"] = hashlib.sha256(evento_string.encode('utf-8')).hexdigest()
    
    return evento

def enviar_telimetria():
    """
    Bucle princial para la simulacion del envio continuo de datos en un entorno real,
    aqui se integraria el cliente MQTT o la llamada a la API REST
    """
    print("Iniciando simulador de nodo Edge (Ctrl+C para detener)...\n")
    try:
        while True:
            nuevo_evento = generar_evento()
            print(json.dumps(nuevo_evento, indent=2))

            #Pausa de 1 segundo para evitar saturacion en pruebas
            time.sleep(1)
    except KeyboardInterrupt:
        print(""
        "\nSimulacion detenida por el usuario.")


if __name__ == "__main__":
    enviar_telimetria()