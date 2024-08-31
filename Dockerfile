# Usa una imagen base oficial de Python
FROM python:3.12.5-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que la aplicación Flask se ejecutará
EXPOSE 5000

# Define la variable de entorno para Flask
ENV FLASK_APP=api_login.py
ENV FLASK_RUN_HOST=0.0.0.0

# Ejecuta la aplicación Flask
CMD ["flask", "run"]
