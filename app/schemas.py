from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str | None = None
    
class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass
    id: int

class TodoDelete(BaseModel):
    # pass
    id: int

    class Config:
        orm_mode = True


# from pydantic import BaseModel

# class TodoCreate(BaseModel):
#     title: str
#     description: str | None = None

# class TodoUpdate(BaseModel):
#     title:str
#     description: str | None = None

# class TodoDelete(BaseModel):
#     id: int
    

#     class Config:
#         orm_mode = True
