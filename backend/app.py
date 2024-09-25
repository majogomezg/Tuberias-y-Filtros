from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import re
import uuid
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

host = os.getenv("BROKER_HOST")
if host == None:
    host = "localhost"

# Configuración del productor Kafka
producer = KafkaProducer(
    bootstrap_servers=f'{host}:9092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Almacenamiento temporal en memoria (simulación de base de datos)
usuarios = {}
tareas = {}

# Validar correo electrónico
def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, email)

# Ruta para crear un usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    if not data.get('nombre') or not data.get('email'):
        return jsonify({'error': 'Nombre y correo electrónico son requeridos'}), 400
    if not validar_email(data['email']):
        return jsonify({'error': 'Correo electrónico no válido'}), 400
    user_id = str(uuid.uuid4())
    usuarios[user_id] = {'id': user_id, 'nombre': data['nombre'], 'email': data['email']}
    return jsonify({'message': 'Usuario creado', 'usuario': usuarios[user_id]}), 201

# Ruta para listar usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({'usuarios': list(usuarios.values())}), 200

# Ruta para obtener usuario por id
@app.route('/usuarios/<user_id>', methods=['GET'])
def obtener_usuario_id(user_id):
    if user_id not in usuarios:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify({'message': 'Usuario encontrado', 'usuario': usuarios[user_id]}), 200



# Ruta para actualizar un usuario
@app.route('/usuarios/<user_id>', methods=['PUT'])
def actualizar_usuario(user_id):
    data = request.json
    if user_id not in usuarios:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    if data.get('email') and not validar_email(data['email']):
        return jsonify({'error': 'Correo electrónico no válido'}), 400
    usuarios[user_id].update(data)
    return jsonify({'message': 'Usuario actualizado', 'usuario': usuarios[user_id]}), 200

# Ruta para eliminar un usuario
@app.route('/usuarios/<user_id>', methods=['DELETE'])
def eliminar_usuario(user_id):
    if user_id not in usuarios:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    del usuarios[user_id]
    return jsonify({'message': 'Usuario eliminado'}), 200

# Ruta para crear una tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.json
    if not data.get('descripcion'):
        return jsonify({'error': 'Descripción de la tarea es requerida'}), 400
    if not data.get('usuario_id') or data['usuario_id'] not in usuarios:
        return jsonify({'error': 'ID de usuario no válido o inexistente'}), 400
    task_id = str(uuid.uuid4())
    tareas[task_id] = {'id': task_id, 'descripcion': data['descripcion'], 'usuario_id': data['usuario_id']}
# Enviar tarea a Kafka
    producer.send('task_topic', tareas[task_id])
    return jsonify({'message': 'Tarea creada y enviada para procesamiento', 'tarea': tareas[task_id]}), 201

# Ruta para listar tareas
@app.route('/tareas', methods=['GET'])
def listar_tareas():
    return jsonify({'tareas': list(tareas.values())}), 200

# Ruta para actualizar una tarea
@app.route('/tareas/<task_id>', methods=['PUT'])
def actualizar_tarea(task_id):
    data = request.json
    if task_id not in tareas:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    if not data.get('descripcion'):
        return jsonify({'error': 'Descripción de la tarea es requerida'}), 400
    tareas[task_id].update(data)
    return jsonify({'message': 'Tarea actualizada', 'tarea': tareas[task_id]}), 200

# Ruta para eliminar una tarea
@app.route('/tareas/<task_id>', methods=['DELETE'])
def eliminar_tarea(task_id):
    if task_id not in tareas:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    del tareas[task_id]
    return jsonify({'message': 'Tarea eliminada'}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
