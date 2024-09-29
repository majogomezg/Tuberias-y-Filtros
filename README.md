# Guía de Despliegue para la Aplicación de Gestión de Tareas y Usuarios

Esta guía proporciona todos los pasos necesarios para desplegar la Aplicación de Gestión de Tareas y Usuarios, que incluye una interfaz web, servicios de backend para la validación y gestión de datos, y servicios de mensajería y almacenamiento usando Kafka y Redis.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Docker
- Docker Compose
- Python (Versión 3.8 o superior)
- Node.js y npm (para el frontend)

## Configuración del Entorno

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. **Clonar el Repositorio**
   Configuración de Variables de Entorno
   ```bash
   cp .env.example .env

# Instalación de Dependencias
Backend

Navega al directorio del backend y instala las dependencias de Python:
bash
Copy code
cd backend
pip install -r requirements.txt
Frontend

Navega al directorio del frontend y instala las dependencias de Node.js:
bash
Copy code
cd ../frontend
npm install
# Despliegue con Docker Compose
Construir y Levantar los Contenedores
Desde el directorio raíz del proyecto, ejecuta:
bash
Copy code
docker-compose up --build
# Verificación
Acceso a la Aplicación Web
Abre tu navegador y visita http://localhost:4321 para acceder a la interfaz de la aplicación.
Verificación de Servicios
Utiliza herramientas como docker ps para asegurarte de que todos los contenedores están corriendo adecuadamente.
Revisa los logs de los contenedores en caso de cualquier error:
bash
Copy code
docker logs nombre_del_contenedor
# Soporte
Si encuentras problemas durante el despliegue o la ejecución de la aplicación, por favor, crea un issue en el repositorio de GitHub o contacta al equipo de soporte a través de mariagomezg@javeriana.edu.co.

   
