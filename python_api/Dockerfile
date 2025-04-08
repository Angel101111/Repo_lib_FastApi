# Usa una imagen oficial de Python
FROM python:3.11

# Crea el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir fastapi uvicorn

# Expone el puerto
EXPOSE 8000

# Ejecuta la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
