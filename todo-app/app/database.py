# 인메모리 저장소
# 인메모리 CRUD - 데이터베이스 연결전에 메모리에 데이터를 저장하는 방식으로 CRUD 구현
from datetime import datetime
from app.models import Todo

# 인메모리 데이터 저장소
todos_db: dict[int, Todo] = {}
todo_id_counter: int = 1

def get_next_id() -> int:
    """다음 ID를 반환하고 카운터 증가"""
    global todo_id_counter
    current_id = todo_id_counter
    todo_id_counter += 1
    return current_id

def reset_db() -> None:
    """테스트용: DB 초기화"""
    global todos_db, todo_id_counter
    todos_db = {}
    todo_id_counter = 1