from kafka import KafkaProducer
import json

def configurar_kafka(host):
    print("Connecting to Kafka on:", f'{host}:9092')
    return KafkaProducer(
        bootstrap_servers=f'{host}:9092', 
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )