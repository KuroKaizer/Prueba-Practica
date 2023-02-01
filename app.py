#Librerias y paquetes
from fastapi import FastAPI
from routes.estudiantes import estudiante

app = FastAPI()

app.include_router(estudiante)