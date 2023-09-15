from pydantic import BaseModel

# Create Person Schema (Pydantic Model)
class PersonCreate(BaseModel):
    name: str

# Complete Person Schema (Pydantic Model)
class Person(BaseModel):
    user_id: int
    name: str

    class Config:
        from_attributes = True

class UpdatePersonRequest(BaseModel):
    name: str
