from fastapi import APIRouter, status
from app.models import Todo, TodoCreate, TodoUpdate
from app import crud
from app.exceptions import TodoNotFoundError

# API Router는 라우터 모듈화 나중에 메인 앱에 등록
# prefix - 모든 경로 앞에 /todos 추가
# tags=["todos"] -Swagger UI에서 그룹화
# HTTP 요청 처리

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    """
    할 일을 생성합니다.
    
    - title: 할 일 제목 (필수, 1~100자)
    - description: 상세 설명 (선택)
    """
    return crud.create_todo(todo)

@router.get("", response_model=list[Todo])
def read_todos(completed: bool | None = None):
    """
    할 일 목록 조회
    - completed : True(완료), False(미완료), None(전체)
    """
    return crud.get_todos(completed=completed)

@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    """특정 할 일 조회"""
    todo = crud.get_todo(todo_id)
    if not todo:
        raise TodoNotFoundError(todo_id)
    return todo

@router.patch("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoUpdate):
    """할 일 수정"""
    updated = crud.update_todo(todo_id, todo)
    if not updated:
        raise TodoNotFoundError(todo_id)
    return updated

@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    """할 일 삭제"""
    deleted = crud.delete_todo(todo_id)
    if not deleted:
        raise TodoNotFoundError(todo_id)
    return {"message": "삭제되었습니다", "deleted": deleted}
