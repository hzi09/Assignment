class Person :
    # 객체 생성시 이름, 성별, 나이 초기화
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # name, gender, age 값을 출력하는 기능을 구현
    def display(self):
        # 이름과 성별은 같은 행에 출력하고, 나이는 다음 행에 출력
        print(f'이름 :{self.name}, 성별 : {self.gender}\n나이 : {self.age}')

# 사용자로부터 나이, 이름, 성별을 각각 입력 받음
a = int(input("나이: "))
b = str(input("이름: "))
c = str(input("셩별: "))

# Person()을 호출
answer = Person(b, c, a)

# display()를 호출하여 값 출력하기
answer.display()