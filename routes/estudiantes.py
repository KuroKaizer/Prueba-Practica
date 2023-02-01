#Creacion de Ruta estudiantes
from fastapi import APIRouter

estudiante = APIRouter()

@estudiante.get("/estudiantes")
def helloworld():
    return "hello world"