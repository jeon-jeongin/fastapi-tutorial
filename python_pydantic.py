from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator

app = FastAPI()

# pydantic은 가능하면 타입을 자동으로 변환
# Field를 사용하면 필드에 추가 정보를 설정 가능
class User(BaseModel):
    name: str = Field(description="사용자 이름")
    age: int
    email: str | None = None  # Optional 필드(있을 수도 없을 수도 있음)

@app.post("/users")
def create_user(user: User):
    return {"message": f"{user.name}님이 등록되었습니다", "user": user}

# 객체 생성
user = User(name="홍길동", age=25, email="hong@example.com")
print(user.name) #홍길동
print(user.age) #25

# 딕셔너리에서 생성
data = {"name": "김철수", "age": 30, "email": "kim@example.com"}
user = User(**data)
print(user.name) #김철수

# 딕셔너리로 변환
user = User(name="홍길동", age=25, email="hong@example.com")
print(user.model_dump())
# {'name': '홍길동', 'age': 25, 'email': 'hong@example.com'}

# 검증 에러 - 잘못된 데이터를 넣으면 에러가 발생
try:
    user = User(name="홍길동", age="스물다섯", email="hong@example.com")
except Exception as e:
    print(e)

# 자기 참조 모델 - 댓글의 대댓글처럼 자기 자신을 참조하는 구조
from __future__ import annotations

class Comment(BaseModel):
    content: str
    author: str
    replies: list[Comment] = [] # 자기 자신의 리스트
# from __future__ import annotations를 추가해야 자기 참조 가능

# 복잡한 검증 로직 @field_validator로 구현
class User(BaseModel):
    username: str
    password: str

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        """
        isalpha : 문자열이 영어 혹은 한글로 되어있으면 참, 아니면 거짓
        isalnum : 문자열이 영어, 한글 혹은 숫자로 되어있으면 참, 아니면 거짓
        """
        if not v.isalnum():
            """raise : 에러를 발생시켜서 실행을 중단 처리"""
            raise ValueError("username은 영문자와 숫자만 허용됩니다.")
        return v
    
    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("password는 8자 이상이어야 합니다.")
        """any() 하나라도 True가 있으면 True : Javascript에서 some과 동일"""
        if not any(c.isupper() for c in v):
            raise ValueError("password는 대문자를 포함해야 합니다")
        if not any(c.isdigit() for c in v):
            raise ValueError("password는 숫자를 포함해야 합니다")
        return v
    
#  여러 필드를 함께 검증 @model_validator로 구현
class DataRange(BaseModel):
    start_date: str
    end_date: str

    """mode='after' 모든 필드가 먼저 검증된 후에 validator가 실행"""
    @model_validator(mode="after")
    def check_dates(self):
        if self.start_date > self.end_date:
            raise ValueError("start_date는 end_date보다 이전이어야 합니다")
        return self