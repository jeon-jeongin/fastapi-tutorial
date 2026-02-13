def test_read_root(client):
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "게시판 API에 오신 것을 환영합니다"}
