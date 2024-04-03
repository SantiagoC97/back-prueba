from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine, Base
from routers.soccer import soccer_router
from routers.auth import auth_router

# Estamos creando una instancia de la clase FastAPI
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(soccer_router)
app.include_router(auth_router)

# Cambios a la documentacion
app.title = "FIFA" 
app.version = "2024"

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['Inicio']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Welcome FIFA 2024 </h1>")