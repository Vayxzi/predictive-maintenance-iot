import json
import time
import random
import hashlib
from datetime import datetime

def generar_evento():
    # Distribución controlada: 70% normal, 20% leve, 10% crítico 
    prob = random.random()
    
    if prob < 0.70:
        tipo_evento = "trafico_normal"
        severidad = random.randint(1, 2) # Severidad baja
        payload = {"status": "ok", "cpu_temp": round(random.uniform(40.0, 55.0), 2)}
    elif prob < 0.90:
        tipo_evento = "anomalia_leve"
        severidad = random.randint(3, 4) # Severidad media
        payload = {"status": "warning", "cpu_temp": round(random.uniform(75.0, 85.0), 2), "error": "latencia_alta"}
    else:
        tipo_evento = "evento_critico"
        severidad = 5 # Severidad máxima
        payload = {"status": "critical", "alerta": "intento_acceso_reiterado", "origen": "ip_desconocida"}

    # Construcción del evento base 
    evento = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "nodo_id": f"Nodo-IoT-{random.randint(1, 3)}",
        "tipo_evento": tipo_evento,
        "severidad": severidad,
        "payload": payload
    }

    # Generación del hash de integridad (SHA-256) 
    # Se convierte el diccionario a string ordenado para que el hash sea consistente
    evento_string = json.dumps(evento, sort_keys=True)
    hash_integridad = hashlib.sha256(evento_string.encode('utf-8')).hexdigest()
    
    # Se añade el hash al evento final
    evento["hash_integridad"] = hash_integridad

    return evento

if __name__ == "__main__":
    print("Iniciando simulador de nodo Edge (Ctrl+C para detener)...\n")
    try:
        while True:
            nuevo_evento = generar_evento()
            # Imprime el evento en formato JSON para visualizarlo fácil
            print(json.dumps(nuevo_evento, indent=2))
            
            # Pausa de 1 segundo entre eventos (para no saturar la terminal en las primeras pruebas)
            time.sleep(1) 
    except KeyboardInterrupt:
        print("\nSimulación detenida por el usuario.")