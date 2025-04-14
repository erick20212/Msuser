# Dockerfile
FROM python:3.10-slim

# 1. Crear el directorio de trabajo
WORKDIR /app

# 2. Copiar e instalar las dependencias
COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiar el resto del código
COPY . .

# 4. Exponer el puerto 5000 (Flask por defecto)
EXPOSE 5000

# 5. Ejecutar la aplicación Flask
CMD ["python", "run.py"]
