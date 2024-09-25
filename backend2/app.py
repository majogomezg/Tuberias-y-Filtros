import logging
from kafka import KafkaConsumer
import redis
import json
from dotenv import load_dotenv
import os
import time



# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("backend2.log"),
        logging.StreamHandler()
    ]
)

# Conectar a Redis en Docker (nombre del servicio como host)
try:
    redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
    redis_client.ping()
    logging.info("Conectado a Redis con éxito.")
except redis.ConnectionError:
    logging.error("No se pudo conectar a Redis.")

load_dotenv()

# Si no se encuentra la variable de entorno BROKER_HOST, usar "broker" en lugar de "localhost"
host = os.getenv("BROKER_HOST", "broker")
if host == None:
    host = "localhost"
    logging.info(f"Usando host predeterminado para Kafka: {host}")

time.sleep(10)  # Esperar 10 segundos antes de conectarse a Kafka
consumer = KafkaConsumer(
    'task_topic',
    bootstrap_servers=f'{host}:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)




# Configuración del consumidor de Kafka
try:
    consumer = KafkaConsumer(
    'task_topic',
    bootstrap_servers=f'{host}:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
 )

    logging.info("Conectado a Kafka con éxito.")
except Exception as e:
    logging.error(f"No se pudo conectar a Kafka: {e}")
# Procesar los mensajes de Kafka y guardarlos en Redis
for message in consumer:
    task_data = message.value
    task_id = task_data.get('id')
    
    logging.info(f"Mensaje recibido de Kafka: {task_data}")

    if task_id:
        try:
            # Guardar tarea en Redis usando el ID como clave
            redis_client.hset('tasks', task_id, json.dumps(task_data))
            logging.info(f"Tarea {task_id} guardada en Redis con éxito.")
        except Exception as e:
            logging.error(f"Error al guardar la tarea en Redis: {e}")
    else:
        logging.warning("ID de tarea no encontrado en el mensaje recibido.")
