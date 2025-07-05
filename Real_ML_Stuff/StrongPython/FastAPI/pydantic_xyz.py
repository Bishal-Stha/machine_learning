from pydantic import BaseModel, EmailStr, ValidationError

class Register(BaseModel):
    username: str
    email: EmailStr

try:
    user = Register(username="bob", email="bishal@gmail.com") #type: ignore
    print(user.model_dump_json()) #type: ignore
    print(user.model_dump()) #type: ignore
except ValidationError as e:
    print(e)
