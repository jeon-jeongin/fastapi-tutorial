from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

# Generic을 사용하면 어떤 타입이든 items 담을 수 있음
class PaginatedResponse(BaseModel, Generic[T]):
    """페이지네이션 응답"""
    items: list[T]
    total: int
    page: int
    size: int
    pages: int  # 전체 페이지 수
