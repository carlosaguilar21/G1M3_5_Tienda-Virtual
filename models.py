from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    lastname: str
    email: str

class UserModel(BaseModel):
    uid: str
    user: str
    name: str
    lastname: str
    email: str
    password: str