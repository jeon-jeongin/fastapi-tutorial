from fastapi import APIRouter, status, Depends
from app.models import Todo, TodoCreate, TodoUpdate
from app import crud
from app.dependencies import get_todo_or_404, PaginationParams

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
def read_todos(completed: bool | None = None, pagination:PaginationParams = Depends()):
    """
    할 일 목록 조회
    - completed : True(완료), False(미완료), None(전체)
    """
    todos = crud.get_todos(completed=completed)
    # 슬라이싱(slicing) 문법 - 리스트에서 원하는 범위만 잘라내는 것
    # 리스트[시작:끝]
    return todos[pagination.skip:pagination.skip + pagination.limit]

@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo: Todo = Depends(get_todo_or_404)):
    """특정 할 일 조회"""
    return todo

@router.patch("/{todo_id}", response_model=Todo)
def update_todo(todo_update: TodoUpdate, todo: Todo = Depends(get_todo_or_404)):
    """할 일 수정"""
    return crud.update_todo(todo.id, todo_update)

@router.delete("/{todo_id}")
def delete_todo(todo: Todo = Depends(get_todo_or_404)):
    """할 일 삭제"""
    crud.delete_todo(todo.id)
