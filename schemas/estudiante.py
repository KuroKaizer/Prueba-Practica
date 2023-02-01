def userEntity(item) -> dict:
    return {
            "id": item["id"],
            "Nombre": item["Nombre"],
            "Apellido": item["Apellido"],
            "Edad": item["Edad"],
            "Afinidad Magica": item["Afinidad Magica"],
            "Grimorio": item["Grimorio"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]    