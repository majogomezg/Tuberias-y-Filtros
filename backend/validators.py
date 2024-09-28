import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, email)

def validar_datos_usuario(data):
    if not data.get('nombre') or not data.get('email'):
        return False, "Nombre y correo electrónico son requeridos"
    if not validar_email(data.get('email')):
        return False, "Correo electrónico no es válido"
    return True, ""