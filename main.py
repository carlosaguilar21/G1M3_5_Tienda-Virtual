import random
from models import UserRequest, UserModel
UserModel

from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


users = Dict[int, UserModel]
users = {
    1:UserModel(**{
        "uid":"1", 
        "user": "pperez1",
        "name": "Pedro",
        "lastname": "Perez",
        "email": "pedro.perez@gmail.com",
        "password": "123456"
    })
}

@app.get("/login/users")
def read_all():

    return http_response(True, users)

@app.get("/login/auth/{username}/{password}")
def read_user(username: str, password:str):
    user = default_user()
    status = False

    for item in users.values():
        if (item.user == username and item.password == password):
            user = item
            status = True

    return http_response(status, user)

@app.post("/login/create")
def create_user(user_req: UserRequest):
    id = len(users.keys())+1
    user = default_user()
    user.uid = str(id)
    user.user = user_req.name[0: 1] + user_req.lastname + str(id)
    user.password = str(random.randint(123456, 987654))
    user.name = user_req.name
    user.lastname = user_req.lastname
    user.email = user_req.email

    users.update({id:user})

    return http_response(True, user)

def default_user():
    return UserModel(**{
            "uid":"", 
            "user": "",
            "name": "",
            "lastname": "",
            "email": "",
            "password": ""
    })

def http_response(status: bool, data: any):
    if status:
        return {"status": 200, "message": "OK", "data": data}
    else:
        return {"status": 404, "message": "Not Found", "data": ""}