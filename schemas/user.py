from pydantic import BaseModel

class User(BaseModel):
    membresia: str
    password: str