from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from kafka_producer import configurar_kafka
from routes import init_routes

app = Flask(__name__)

def configurar_app():
    load_dotenv()
    host = os.getenv("BROKER_HOST","broker")
    if host == None:
        host = "localhost"
    return host


host = configurar_app()
producer = configurar_kafka(host)

# Inicializar rutas
init_routes(app, producer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
