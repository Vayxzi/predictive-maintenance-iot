# Simulador de Telemetría Edge (IoT)

Este script en Python simula la generación y envío de eventos de telemetría desde nodos IoT (Edge Computing). Actualmente funciona como el motor de generación de datos estructurados para un proyecto en desarrollo orientado al mantenimiento predictivo.

## Habilidades y Tecnologías Aplicadas
- **Lenguaje:** Python 3.
- **Seguridad y Validación:** Firmado de la carga útil (payload) mediante hashes de integridad SHA-256 para asegurar que los datos no sean alterados.
- **Estructuración de Datos:** Generación de eventos en formato JSON, listos para ser consumidos mediante APIs REST o brokers MQTT.
- **Lógica de Simulación:** Distribución probabilística de estados operativos (70% tráfico normal, 20% anomalías térmicas/latencia y 10% alertas críticas de seguridad).

## Próximos Pasos (Roadmap)
- [ ] Integración del flujo de datos con backend para ingesta en tiempo real.
- [ ] Consumo de alertas y automatización de tickets de mantenimiento en ERP (Odoo 19).

## Ejecución local
Para correr el simulador y visualizar la salida de datos en la terminal:
```bash
python simulador_edge.py
