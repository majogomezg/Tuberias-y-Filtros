# Usar una imagen base de Node.js
FROM node:18-alpine

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de la aplicación
COPY . .

# Construir la aplicación (ajusta según tu script de build)
RUN npm run build

# Exponer el puerto de la aplicación
EXPOSE 4321

# Comando para ejecutar la aplicación
CMD ["npm", "run", "start", "--", "--host"]
