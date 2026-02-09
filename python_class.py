# 클래스 정의
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"안녕하세요, {self.name}입니다.")
# class User: - 클래스 정의(클래스명은 대문자로 시작)
# __init__ - 생성자 메서드, 객체가 만들어질 때 자동호출
# self - 객체 자신을 가리킴, 모든 메서드의 첫 번째 매개변수
# greet - 메서드, 클래스 안에 정의된 함수

# 클래스 상속
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}: 멍멍")
    

class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 야옹")

# 사용
dog = Dog("바둑이")
cat = Cat("나비")

dog.speak()  # 바둑이: 멍멍!
cat.speak()  # 나비: 야옹!
# Dog(Animal) - Dog는 Animal을 상속
# Dog, Cat은 Animal의 __init__을 그대로 사용
# speak 메서드는 각 클래스에서 재정의(오버라이딩)

# 데이터 클래스(dataclass) : Python 3.7부터는 dataclass를 사용하면 간단하게 클래스 생성가능
# @dataclass 데코레이터가 __init__ 등을 자동으로 만들어 줌
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str = "" # 기본값

# 사용
user = User("홍길동", 25)
print(user)
# User(name='홍길동', age=25, email='')

print(user.name)  # 홍길동


# 클래스 메서드 (@classmethod) : 클래스 자체를 첫 번째 인자로 받음, 객체를 다른 방식으로 생성할 때 유용
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 User 생성"""
        return cls(data["name"], data["age"])
    
# 정적 메서드 (@staticmethod) : 클래스/객체와 무관한 유틸리티 함수
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
# 객체 없이 호출 가능
result = Calculator.add(3, 5)
print(result)  # 8