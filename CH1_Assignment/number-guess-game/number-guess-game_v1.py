import random as rd

# 1~10 사이의 숫자를 랜덤하게 정하기
n = rd.randint(1,10)
print("1과 10 사이의 숫자를 하나 정했습니다.\n이 숫자는 무엇일까요? ")

# 정답을 맞출때까지 반복됩니다.
while True :
    # 예상 숫자를 입력할 수 있게 함. 숫자가 입력이 되어야 하므로 타입은 int로 변환
    answer = int(input("예상 숫자 : "))

    # 입력한 값이 n보다 작다면, 아래의 print() 출력 후 다시 실행
    if n > answer :
        print("너무 작습니다. 다시 입력하세요.")

    # 입력한 값이 n보다 크다면, 아래의 print() 출력 후 다시 실행
    elif n < answer :
        print("너무 큽니다. 다시 입력하세요.")

    # 위의 두 경우가 아니라면 "정답입니다"를 출력하고 실행 종료
    else :
        print("정답입니다!")
        break