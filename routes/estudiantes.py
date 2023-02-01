#Creacion de Ruta estudiantes
from fastapi import APIRouter
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
def actualizar_solicitud(id: str, user:User):
    conn.local.user.find_one_and_update({"id":id}, {"$set": dict(user)})
    return userEntity(conn.local.user.find_one)

#Actaulizar estatus de la solicitud
@estudiante.put("/estudiante")
def actualizar_estatus(id: str, user:User):
    conn.local.user.find_one_and_update({"id":id}, {"$set": dict(user)})
    return userEntity(conn.local.user.find_one)

#Consultar todas las solicitudes
@estudiante.get("/estudiantes")
def consultar_todo():
    return usersEntity(conn.local.user.find())

#Consultar asignaciones de Grimorios
@estudiante.get("/estudiante/{id}")
def consultar_grimorio(id:str):
    return userEntity(conn.local.user.find_one_and_delete({"id":id}))
    

#Eliminar solicitud de ingreso
@estudiante.delete("/estudiante/{id}")
def eliminar_solicitud(id: str):
    userEntity(conn.local.user.find_one_and_delete({"id":id}))
    return "Solicitud eliminada"