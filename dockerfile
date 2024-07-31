# Usa una imagen base oficial de Python
FROM python
#Crea el directorio
RUN mkdir -p /usr/src/app
# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requeriments.txt /app

# Instala las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requeriments.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . /app/

# Expone el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 8000

# Establece la variable de entorno para desactivar el búfer de salida de Python
#ENV PYTHONUNBUFFERED=1

# Ejecuta las migraciones de la base de datos y lanza el servidor de desarrollo
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

