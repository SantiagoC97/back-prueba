# Inventario_FIFA_FastAPI

Descripción

Bienvenido a la API oficial de FIFA 2024.
Esta API brinda una plataforma para acceder al inventario de láminas de los jugadores de fútbol. Construido a partir de FastAPI, compuesta por una serie de endpoints para acceder a los datos de manera rápida y sencilla.

Tecnologías usadas

FastAPI
SQLAlchemy
SQLite
Uvicorn

Instalación y ejecución

Crear un nuevo repositorio en GitHub

Clonar el repositorio desde el PowerShell con el comando:
git clone https://github.com/tu-usuario/nombre-repositorio.git

Se accede a la carpeta donde esta ubicado el proyecto con el comando:
cd .\nombre-carpeta\

Se crea el entorno virtual:
python -m venv venv

Activamos el entorno virtual:
venv\Scripts\activate

Instalamos las dependencias necesarias:
pip install fastapi uvicorn sqlalchemy databases[sqlite] pydantic
pip install -r requirements.txt

Damos inicio al servidor de desarrollo donde esta ubicada la API:
uvicorn main:app --reload

Abrimos el navegador web, visitando la siguiente URL:
http://127.0.0.1:8000/docs

Funcionalidades

Autorizacion de token de validación

get/soccer/{id} : permite buscar las láminas de los jugadores mediante el número del dorsal (id).

put/soccer/{id} : actualiza la lista de láminas ingresadas

delete/soccer/{id} : elimina cualquier lámina deseada

get/soccer/ : permite buscar a los jugadores por medio de la posición del jugador

get/soccer/ : permite buscar a los jugadores por los nombres de cada uno de ellos.

post/soccer/ : es la función principal, la cuál se encarga de ingresar al inventario las láminas deseadas.

token de autenticación y mensaje de inicio, que es el general de la API antes de ingresar a /docs.






