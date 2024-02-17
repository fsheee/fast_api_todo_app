from sqlalchemy import Column,  Integer, String
from .database import Base

class Todo(Base):
    __tablename__ = "todoitem"


    id = Column("id",Integer, primary_key=True)
    title = Column("title",String, index=True)
    description = Column("description",String)