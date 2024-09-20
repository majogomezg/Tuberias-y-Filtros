# Usar una imagen base ligera de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar y instalar las dependencias desde requirements.txt
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente al directorio de trabajo del contenedor
COPY . .

# Comando para ejecutar el Servicio B
CMD ["python", "app.py"]
