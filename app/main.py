from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
# from sqlalchemy.ext.declarative import declarative_base
from .crud import crud_create_todo,get_todos,crud_update_todo,crud_delete_todo
from .models import Todo
from .schemas import TodoCreate,TodoUpdate,TodoDelete
from .database import SessionLocal, engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return crud_create_todo(db=db, todo=todo)

@app.put("/todos/{id}")
def update_todo(id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    # Update the todo item using the provided ID and todo data
    updated_todo = crud_update_todo(db=db, todo_id=id, todo=todo)
    
    # Check if the todo item was successfully updated
    if updated_todo:
        return {"updated_todo": updated_todo, "message": "Todo item successfully updated"}
    else:
        # If the todo item with the provided ID was not found, raise HTTPException
        raise HTTPException(status_code=404, detail="Todo item not found")


@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    # Try to delete the todo item
    try:
        delete_todo = crud_delete_todo(db=db, todo_id=id)
        if delete_todo:
            return  {"delete_todo": delete_todo, "message": "Todo item successfully Deleted"}

        else:
            raise HTTPException(status_code=404, detail="Todo item not found")
    except Exception as e:
        # If an exception occurs, raise an HTTPException with status code 500 (Internal Server Error)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/todos")
def get_todo(db: Session = Depends(get_db)):
    todos = get_todos(db=db)
    return todos



