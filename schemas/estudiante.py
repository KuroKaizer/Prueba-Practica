def estudianteEntity(item) -> dict:
    return {
            "id": item["id"],
            "Nombre": item["Nombre"],
            "Apellido": item["Apellido"],
            "Edad": item["Edad"],
            "Afinidad Magica": item["Afinidad Magica"]
    }