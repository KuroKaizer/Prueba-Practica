def userEntity(item) -> dict:
    return {
            "id": item["id"],
            "Nombre": item["Nombre"],
            "Apellido": item["Apellido"],
            "Edad": item["Edad"],
            "Afinidad_Magica": item["Afinidad_Magica"],
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]    