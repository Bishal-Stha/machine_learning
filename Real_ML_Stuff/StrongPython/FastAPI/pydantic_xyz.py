from pydantic import BaseModel, EmailStr, ValidationError

class Register(BaseModel):
    username: str
    email: EmailStr

try:
    user = Register(username="bob", email="bishal@gmail.com")
    print(user.model_dump_json())
    print(user.model_dump())
except ValidationError as e:
    print(e)
