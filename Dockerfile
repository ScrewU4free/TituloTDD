
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . /app

# Instalar TensorFlow
RUN pip install --no-cache-dir tensorflow

# Exponer el puerto (opcional, si se sirve el modelo)
EXPOSE 8501

# Comando predeterminado para ejecutar el script
CMD ["python", "model_script.py"]
