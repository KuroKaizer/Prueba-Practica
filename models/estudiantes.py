from pydantic import BaseModel

class User(BaseModel):
    id: str
    Nombre: str
    Apellido: str
    Edad: int
    Afinidad_Magica:str