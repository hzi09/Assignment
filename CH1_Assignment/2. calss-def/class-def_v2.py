class Person :
    # 객체 생성시 이름, 성별, 나이 초기화
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # name, gender, age 값을 출력하는 기능을 구현
    def display(self):
        # 이름과 성별은 같은 행에 출력하고, 나이는 다음 행에 출력
        print(f'이름 : {self.name}, 성별 : {self.gender}\n나이 : {self.age}')

    # 나잇대에 맞는 인사 메시지를 출력
    def greet(self):
        # 19세 초과이면 성인
        if self.age > 19 :
            value = '성인'
        # 0~19세이면 미성년자
        elif self.age in range(0, 20) :
            value = '미성년자'
        # 음수는 잘못된 값으로 ????를 출력
        else :
            value = '????'
        print(f'안녕하세요, {self.name}님! {value}이시군요!')

# 사용자로부터 나이, 이름을 각각 입력 받음
user_age = int(input("나이: "))
user_name = input("이름: ")

# 잘못된 성별이 입력되면 오류 메시지 출력하고, 올바른 성별을 입력받을 때까지 반복
while True :
    # 성별을 입력받음
    user_gender = input("성별: ")
    #성별이 male, female이면 코드 종료!
    if user_gender == 'male' or user_gender == 'female' :
        break
    # 성별이 male, female이 아니면 오류메시지 출력 후 while문 다시 반복
    else :
        print("잘못된 성별을 입력했습니다. 'male' 또는 'female'을 입력하세요. ")
        continue

# Person()을 호출
answer = Person(user_name, user_gender, user_age)

# display()를 호출하여 값 출력하기
answer.display()

# greet()를 호출하여 인사 메시지 출력하기
answer.greet()
