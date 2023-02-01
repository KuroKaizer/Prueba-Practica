from pydantic import BaseModel
import random as rd

class User(BaseModel):
    id: str
    Nombre: str
    Apellido: str
    Edad: int
    Afinidad_Magica:str
    Grimonrio: str

    def aleatorio():
        grimorios = ["Sinceridad","Esperanza","Amor","Buena Fortuna","Desesperacion"]
        seleccion = rd.choice(grimorios)
        return seleccion
