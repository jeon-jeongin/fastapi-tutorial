from fastapi import APIRouter, Depends
# 의존성 주입 - 함수가 필요한 것을 외부에서 주입받는 패턴

router = APIRouter()

# 공통 매개변수 추출
# Before - 반복되는 코드
@router.get("/todos")
def read_todos(skip: int = 0, limit: int = 10):
    ...

@router.get("/users")
def read_users(skip: int = 0, limit: int = 10):
    ...

# After - 의존성으로 추출
def pagination_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@router.get("/todos")
def read_todos(pagination: dict = Depends(pagination_params)):
    skip = pagination["skip"]
    limit = pagination["limit"]
    ...

@router.get("/users")
def read_users(pagination: dict = Depends(pagination_params)):
    ...


# 클래스 의존성
class Pagination:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit

@router.get("/todos")
# Depends()에 인자가 없으면 타입 힌트의 클래스를 사용
def read_todos(pagination: Pagination = Depends()):
    return crud.get_todos()[pagination.skip:pagination.skip + pagination.limit]