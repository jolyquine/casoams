Documentancion para implementacion de este proyecto.

1. Crear la imagen
docker build -t casoams .

2. Ubicar la ruta del proyecto y ejecutar el contenedor conla imagen creada
docker run -it -d --name casoams -p 8080:8080 -p 8000:8000  -v D:/Proyectos/1/CasoAMS/app:/app casoams
docker run -it -d --name casoams -p 8080:8080 -p 8000:8000  -v directorio-local-app:/app casoams


3. Ejecutar los siguientes comandos para los modelaos de base de datos

python3 manage.py makemigrations
python3 manage.py migrate

4. Ejecutar la migracion de la api cliente


python3 manage.py makemigrations
python3 manage.py migrate

5. Crear el usuario administrador
python3 manage.py createsuperuser

6. Levantar el servidor en desarrollo, indicando el puerto

python3 manage.py runserver 0:8080

5. Consultar al endponit http://127.0.0.1:8080/api/clientes/
Lista los usuarios creados en la base de datos


