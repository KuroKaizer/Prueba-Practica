#Creacion de Ruta estudiantes
from fastapi import APIRouter

estudiante = APIRouter()

#Enviar solicitud de ingreso
@estudiante.post("/estudiantes")
def enviar_solicitud():
    return "hello world"

#Actualizar solicitud de ingreso
@estudiante.put("/estudiantes")
def actualizar_solicitud():
    return "hello world"

#Actaulizar estatus de la solicitud
@estudiante.put("/estudiantes")
def actualizar_estatus():
    return "hello world"

#Consultar todas las solicitudes
@estudiante.get("/estudiantes")
def consultar_todo():
    return "hello world"

#Consultar asignaciones de Grimorios
@estudiante.get("/estudiantes")
def consultar_grimorio():
    return "hello world"

#Eliminar solicitud de ingreso
@estudiante.delete("/estudiantes")
def eliminar_solicitud():
    return "hello world"                    