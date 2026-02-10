# SQLite 데이터 베이스
from sqlmodel import SQLModel, Session, create_engine
from app.config import DATABASE_URL

# 엔진 생성
engine = create_engine(
    DATABASE_URL,
    echo=True,  # SQL 로그 출력 (개발용)
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {} # SQLite 전용 설정 (check_same_thread 멀티스레드 허용)
)

def create_db_and_tables():
    """데이터베이스와 테이블 생성"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    데이터베이스 세션 제공 (의존성)
    - with : 자원을 자동으로 정리해주는 문법
    - yield : 값을 반환하고 일시정시, 나중에 이어서 실행
    """
    with Session(engine) as session: # DB 세션 열기
        yield session # 세션을 넘겨주고 대기(요청 처리 동안) -> 요청 끝나면 with문이 자동으로 세션 닫기
