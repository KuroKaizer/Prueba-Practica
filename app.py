#Librerias y paquetes
from fastapi import FastAPI
from routes.estudiantes import estudiante

app = FastAPI(
    title="IA Interactive | Prueba Práctica | Python Developer"
)

app.include_router(estudiante)