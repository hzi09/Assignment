import random as rd

# 1~10 사이의 숫자를 랜덤하게 정하기
n = rd.randint(1,10)
print("1과 10 사이의 숫자를 하나 정했습니다.\n이 숫자는 무엇일까요? ")

# 정답을 맞출때까지 반복됩니다.
while True :
    # 예상 숫자를 입력할 수 있게 함. 숫자가 입력이 되어야 하므로 타입은 int로 변환
    answer = int(input("예상 숫자 : "))

    # 입력한 값이 1과 10 사이의 숫자이면 아래의 코드를 실행
    if answer in range(1, 11) :
        # 입력한 값이 n보다 작다면, 아래의 print() 출력 후 다시 실행
        if n > answer :
            print("너무 작습니다. 다시 입력하세요.")

        # 입력한 값이 n보다 크다면, 아래의 print() 출력 후 다시 실행
        elif n < answer :
            print("너무 큽니다. 다시 입력하세요.")

        # 위의 두 경우가 아니라면 "정답입니다"를 출력하고 실행 종료
        else :
            print("정답입니다!")

            # 정답을 맞추면 게임을 다시 시작할지 결정
            message = input("게임을 다시 시작하시겠습니까? (y/n) :")

            # y이나 Y가 입력되면 while문을 다시 실행하여 게임을 다시 시작
            if message == 'y' or message == 'Y' :
                # 랜덤으로 숫자를 다시 설정함
                n = rd.randint(1, 10)
                print("1과 10 사이의 숫자를 하나 정했습니다.\n이 숫자는 무엇일까요? ")
                continue

            # n이나 N이 입력되면 while문을 종료하여 게임 종료
            elif message == 'n' or message == 'N' :
                print("게임을 종료합니다. 즐거우셨나요? 또 만나요!")
                break

            # 문자가 잘못입력되면, 게임 종료
            else :
                print("잘못된 문자입니다. 게임이 종료됩니다.")
                break

    # 입력한 값이 범위를 벗어나면 경고 메세지!
    else :
        print("범위에서 벗어났습니다!! 1부터 10까지 범위 안에서 다시 정해주세요!!")