from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.routers import todos
from app.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    """앱 시작/종료 시 실행되는 코드"""
    # 시작 시 테이블 생성
    create_db_and_tables()
    yield
    # 종료 시 : (필요하면 정리 코드)

# lifespan : 앱의 생명주기 이벤트를 처리
app = FastAPI(
    title="TODO API",
    description="할 일 관리 API",
    version="1.0.0",
    lifespan=lifespan
)

# 라우터 등록
app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "TODO API에 오신 것을 환영합니다"}

# 전역 예외 핸들러 - 특정 예외를 전역적으로 처리할 수 있음
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

# 검증 에러 커스터 마이징 - Pydantic 검증 에러의 응답 형식을 변경
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(x) for x in error["loc"]),
            "message": error["msg"]
        })

    return JSONResponse(
        status_code=422,
        content={"errors": errors}
    )