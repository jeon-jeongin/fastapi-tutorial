# fastapi 패키지에서 FastAPI 클래스를 가져옴
from fastapi import FastAPI

# FastAPI 인스턴스를 만듬, app이 웹 어플리케이션
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/hello")
def say_hello():
    return {"greeting": "안녕하세요"}

# 함수에 독스트링을 추가하면 Swagger UI에 표시
# 상세한 문서를 만들기 위해서는 summary, description 파라미터를 사용 가능
@app.get(
    "/items",
    summary="아이템 목록 조회",
    description="저장된 모든 아이템의 목록을 반환합니다."
)
def read_items():
    """
    모든 아이템 목록을 반환합니다.

    - 인증 필요 없음
    - 최대 100개까지 반환
    """
    return {"items": ["사과", "바나나", "오렌지"]}

# 태그로 그롭화하기 - 엔드포인트가 많아지면 태그로 그룹화 가능
@app.get("/users", tags=["users"])
def read_users():
    """사용자 목록 조회"""
    return {"users": []}

# 경로 매개변수 - URL 경로에서 데이터를 받는 방법
@app.get("/users/{user_id}", tags=["users"])
# user_id: int 타입 힌트로 자동변환 처리
def read_user(user_id: int):
    """특정 사용자 조회"""
    return {"user_id": user_id}

@app.get("/items", tags=["items"])
def read_items():
    """아이템 목록 조회"""
    return {"items": []}

# Enum으로 값 제한 - 특정 값만 허용하고 싶을 때 Enum을 사용
from enum import Enum

class ItemCategory(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    food = "food"
    
@app.get("/items/{category}")
def read_items_by_category(category: ItemCategory):
    return {"category": category, "message": f"{category.value} 카테고리 아이템"}