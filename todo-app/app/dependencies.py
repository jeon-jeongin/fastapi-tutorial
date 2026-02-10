from fastapi import Depends, HTTPException, status
from app.models import Todo
from app import crud

def get_todo_or_404(todo_id: int) -> Todo:
    """할 일을 조회하거나 404 에러를 반환"""
    todo = crud.get_todo(todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID {todo_id}인 할 일을 찾을 수 없습니다."
        )
    return todo

