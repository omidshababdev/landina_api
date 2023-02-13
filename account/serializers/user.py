def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "type": user["type"],
        "password": user["password"],
        "createdAt": user["createdAt"],
        "updatedAt": user["updatedAt"]
    }


def userResponseEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "type": user["type"],
        "createdAt": user["createdAt"],
        "updatedAt": user["updatedAt"]
    }


def embeddedUserResponse(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"],
        "username": user["username"],
        "type": user["type"],
        "image": user["image"]
    }


def userListEntity(users) -> list:
    return [userEntity(user) for user in users]

