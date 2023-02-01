#Creacion de Ruta estudiantes
from fastapi import APIRouter,Response
from config.db import conn

from schemas.estudiante import userEntity, usersEntity
from models.estudiantes import User

estudiante = APIRouter()

#Enviar solicitud de ingreso
@estudiante.post("/estudiante")
def enviar_solicitud(user: User):
    new_user = dict(user)
    id = conn.local.user.insert_one(new_user).inserted_id
    return "recibido"
    
    
#Actualizar solicitud de ingreso
@estudiante.put("/estudiante/{id}")
def actualizar_solicitud():
    return "hello world"

#Actaulizar estatus de la solicitud
@estudiante.put("/estudiante")
def actualizar_estatus():
    return "hello world"

#Consultar todas las solicitudes
@estudiante.get("/estudiantes")
def consultar_todo():
    return usersEntity(conn.local.user.find())

#Consultar asignaciones de Grimorios
@estudiante.get("/estudiante/{id}")
def consultar_grimorio():
    return "hello world"

#Eliminar solicitud de ingreso
@estudiante.delete("/estudiante/{id}")
def eliminar_solicitud():
    return "hello world"