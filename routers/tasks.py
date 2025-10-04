from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

import schemas, models, security, database

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    dependencies=[Depends(security.get_current_user)],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_task = models.Task(**task.dict(), owner_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    
    now = datetime.utcnow()
    
    expired_tasks = db.query(models.Task).filter(
        models.Task.owner_id == current_user.id,
        models.Task.status == "Pendente",
        models.Task.due_date < now
    ).all()
    
    for task in expired_tasks:
        task.status = "Expirada"
    
    if expired_tasks:
        db.commit()

    tasks = db.query(models.Task).filter(models.Task.owner_id == current_user.id).offset(skip).limit(limit).all()
    return tasks

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task_update: schemas.TaskCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")
    
    for var, value in vars(task_update).items():
        setattr(db_task, var, value) if value else None

    if db_task.status == "Expirada" and not db_task.completed:
        db_task.status = "Pendente"

    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")
        
    db.delete(db_task)
    db.commit()
    return {"detail": "Task deleted successfully"}

@router.patch("/{task_id}/toggle", response_model=schemas.Task)
def toggle_task_completion(task_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this task")
        
    db_task.completed = not db_task.completed
    db_task.status = "Concluída" if db_task.completed else "Pendente"

    db.commit()
    db.refresh(db_task)
    return db_task