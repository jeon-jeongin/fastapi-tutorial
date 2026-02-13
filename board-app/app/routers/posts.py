from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.database import get_session
from app.models import Post, PostCreate, PostUpdate, PostResponse, PostListWithCount
from app.crud import post as post_crud
from app.crud import comment as comment_crud
from app.dependencies import get_post_or_404

router = APIRouter(prefix="/posts", tags=["posts"])

# 임시
def get_current_user_id() -> int:
    return 1

@router.post("", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    post: PostCreate,
    session: Session = Depends(get_session),
    current_user_id: int = Depends(get_current_user_id)
):
    """
    게시글을 작성

    - title : 제목(1~200자)
    - content : 내용
    """
    return post_crud.create_post(session, post, current_user_id)

@router.get("", response_model=list[PostListWithCount])
def read_posts(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session)
):
    """게시글 목록을 조회 (최신순으로 정렬)"""
    posts = post_crud.get_posts(session, skip=skip, limit=limit)

    result = []
    for post in posts:
        post_dict = post.model_dump()
        post_dict["comment_count"] = comment_crud.count_comments_by_post(session, post.id)
        result.append(post_dict)

    return result

@router.get("/{post_id}", response_model=PostResponse)
def read_post(
    post: Post = Depends(get_post_or_404),
    session: Session = Depends(get_session)
):
    """
    게시글을 조회

    조회 시 조회수가 1 증가
    """
    post_crud.increment_views(session, post)
    return post

@router.patch("/{post_id}", response_model=PostResponse)
def update_post(
    post_update: PostUpdate,
    post: Post = Depends(get_post_or_404),
    session: Session = Depends(get_session),
    current_user_id: int = Depends(get_current_user_id)
):
    """게시글을 수정(작성자만 수정 가능)"""
    if post.author_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="수정 권한이 없습니다"
        )
    return post_crud.update_post(session, post, post_update)

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post: Post = Depends(get_post_or_404),
    session: Session = Depends(get_session),
    current_user_id: int = Depends(get_current_user_id)
):
    """게시글을 삭제(작성자만 삭제 가능)"""
    if post.author_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="삭제 권한이 없습니다"
        )
    post_crud.delete_post(session, post)
