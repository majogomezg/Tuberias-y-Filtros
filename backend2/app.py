from kafka import KafkaConsumer
import redis
import json

# Conectar a Redis en Docker (nombre del servicio como host)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Configuración del consumidor de Kafka
consumer = KafkaConsumer(
    'task_topic',  # Nombre del "topic" de Kafka
    bootstrap_servers='broker:9092',  # Cambia a 'broker' que es el nombre del contenedor de Kafka
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Procesar los mensajes de Kafka y guardarlos en Redis
for message in consumer:
    task_data = message.value
    task_id = task_data.get('id')
    
    if task_id:
        # Guardar tarea en Redis usando el ID como clave
        redis_client.hset('tasks', task_id, json.dumps(task_data))
        print(f"Tarea {task_id} guardada en Redis con éxito.")
    else:
        print("ID de tarea no encontrado en el mensaje recibido.")
