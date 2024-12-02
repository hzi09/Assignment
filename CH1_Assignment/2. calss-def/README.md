# 2.  클래스와 함수 사용하기


## 🗂️Directory Structure
- `README.md` : 디렉토리 구조, 과제 내용, 입출력 예시, 문제 풀이
- `class-def_v1` : 메인 과제 코드
- `class-def_v2` : 추가 도전 과제 코드

<br>

## 📝과제 내용
- 이름, 성별, 나이를 입력받고, 이를 출력하는 프로그램을 작성해주세요.

### ⭐처리 조건
- **클래스 정의**
    - `Person`이라는 이름의 클래스를 정의한다.
- **멤버 변수**
    - `name`, `gender`, `age`라는 멤버 변수를 설정한다.
    - 각 변수는 객체가 생성될 때 초기화된다.
        - `name`: 이름을 저장하는 변수 (문자열)
        - `gender`: 성별을 저장하는 변수 (문자열, "male" 또는 "female")
        - `age`: 나이를 저장하는 변수 (정수형)
- **생성자**
    - 생성자 `__init__`를 통해 객체 생성 시 이름, 성별, 나이를 초기화한다.
    - 매개변수로 이름(`name`), 성별(`gender`), 나이(`age`)를 받는다.
- **정보를 출력하는 함수 `display()`**
    - `name`, `gender`, `age` 값을 출력하는 기능을 구현한다.
    - 이름과 성별은 같은 행에 출력하고, 나이는 다음 행에 출력한다.
- **입력 및 출력**
    - 사용자로부터 나이, 이름, 성별을 각각 입력받는다.
    - 입력된 값을 바탕으로 `Person` 객체를 생성하고, `display()` 함수를 통해 객체의 정보를 출력한다.

### ✅입출력 예시
- 사용자 입력 예시
```
나이: 28
이름: 페이커
성별: male
```
- 출력 예시
```
이름: 페이커, 성별: male
나이: 28
```


<br>

## 🔥추가 도전 과제
1. Person 클래스 생성자에서 사용자의 성별 입력값에 대한 유효성 검사를 추가해주세요.
   - `gender` 값이 `male` 또는 `female`로만 입력될 수 있도록 제한하는 로직을 넣으면 됩니다.
   - 잘못된 입력이 들어오면 오류 메시지를 출력하고, 올바른 성별을 입력받을 때까지 반복해서 입력을 받도록 구현할 수 있습니다.
### ✅입출력 예시
```
나이: 28
이름: 페이커
성별: 남성
잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력하세요.
성별: 
```
2. Person 클래스에 나잇대에 맞는 인사 메시지를 출력할 수 있도록 greet() 함수를 추가해주
   - greet() 함수는 age 값에 따라 다음과 같은 메시지를 출력합니다.
### ✅입출력 예시
```
나이: 28
이름: 페이커
성별: male
이름: 페이커, 성별: male
나이: 28
안녕하세요, 페이커! 성인이시군요!
```

<br>

## ✍️ 과제 풀이

1. 클래스 정의 및 멤버 변수 설정

```python
class Person :
    # 객체 생성시 이름, 성별, 나이 초기화
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
```

2. 정보를 출력하는 함수 `display()`
    - 이름과 성별은 같은 행에 출력하고, 나이는 다음 행에 출력

```python
  def display(self):
      # 이름과 성별은 같은 행에 출력하고, 나이는 다음 행에 출력
      print(f'이름 :{self.name}, 성별 : {self.gender}\n나이 : {self.age}')
```

3. 사용자에게 입력받을 수 있도록 `input()` 설정

```python
# 사용자로부터 나이, 이름, 성별을 각각 입력 받음
a = int(input("나이: "))
b = str(input("이름: "))
c = str(input("셩별: "))
```

4. 클래스 호출 및 값 출력하기

```python
# Person()을 호출
answer = Person(b, c, a)

# display()를 호출하여 값 출력하기
answer.display()
```

## 🔥 도전 과제 풀이

✅ 코드에서 삭제한 것 없이 추가만 해주었다.

1. `Person` 클래스에 나잇대에 맞는 인사 메시지를 출력할 수 있도록 `greet()` 함수를 추가
    - `if ~ elif ~ else문`을 사용하여 나이대에 맞는 조건을 줌
        - 19세 초과 : 성인
        - 0~19세 : 미성년자
        - 두가지의 경우가 아니라면 : ????
    - 인사 메시지 출력

```python
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
```

2. `Person` 클래스 생성자에서 사용자의 성별 입력값에 대한 유효성 검사를 추가
    - while문을 사용하여 gender입력을 while문 안에 넣음
        - `male` 또는  `female` 이 입력될때까지 입력을 반복
    - if ~ else문을 사용하여 조건을 줌
        - `male` 또는  `female`이 입력되면 `break`를 사용하여 실행 종료
        - 그렇지 않으면 오류메세지를 출력하고 `continue`를 사용하여 while문 다시 실행

```python
# 잘못된 성별이 입력되면 오류 메시지 출력하고, 올바른 성별을 입력받을 때까지 반복
while True :
    # 성별을 입력받음
    user_gender = input("성별: ")
    #성별이 male, female이면 코드 종료!
    if user_gender in ['male', 'female'] :
        break
    # 성별이 male, female이 아니면 오류메시지 출력 후 while문 다시 반복
    else :
        print("잘못된 성별을 입력했습니다. 'male' 또는 'female'을 입력하세요. ")
        continue
```

3. `greet()`함수를 호출

```python
# greet()를 호출하여 인사 메시지 출력하기
answer.greet()
```