# 논리 연산자 : 여러 조건을 조합할 때 사용

# and : 둘 다 참이어야 참
age = 25
has_id = True
if age >= 18 and has_id:
    print("입장 가능")

# or : 하나만 참이어도 참
is_member = False
has_coupon = True
if is_member or has_coupon:
    print("할인 적용")

# not : 참/거짓을 뒤집음
is_banned = False
if not is_banned:
    print("서비스 이용 가능")

# range() 함수는 숫자 시퀀스를 만듬
for i in range(5):
    print(i) # 0 1 2 3 4

# range(시작, 끝, 간격)
for i in range(1, 4):
    print(i) # 1 2 3

# 가변 인자 (*args) : 인자 개수가 정해지지 않을 때 사용
# *numbers : 전달된 모든 인자는 튜플로 받음
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2))           # 3
print(add_all(1, 2, 3, 4, 5))  # 15

# 키워드 가변 인자 (**kwargs)
# **info : 이름이 지정된 가변인자를 딕셔너리로 받음
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="홍길동", age=25, city="서울")

# 람다 함수 : 간단한 함수를 한 줄로 작성
# 일반 함수
def add(a, b):
    return a + b

# 람다 함수
add = lambda a, b: a + b
print(add(3, 5))