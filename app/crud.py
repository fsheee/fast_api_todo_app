from sqlalchemy.orm import Session

from .models import Todo
from .schemas import TodoCreate,TodoUpdate,TodoDelete


def get_todo(db: Session, id: int):
    return db.query(Todo).filter(Todo.id == id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()


def crud_create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


#
def crud_update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    # Query the database to find the todo item by its ID
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    # Check if the todo item exists
    if db_todo:
        # Update the attributes of the todo item
        db_todo.title = todo.title
        db_todo.description = todo.description
        db.add(db_todo)
        # Commit the changes to the database
        db.commit()
        
        # Refresh the todo item to reflect changes
        db.refresh(db_todo)
        
        # Return the updated todo item
        return db_todo
 

def crud_delete_todo(db: Session, todo_id: int):
    # Query the database to find the todo item by its ID
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    # Check if the todo item exists
    if db_todo:
        # Delete the todo item from the database
        db.delete(db_todo)
        db.commit()
        return db_todo