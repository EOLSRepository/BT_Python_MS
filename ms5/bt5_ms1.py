# 5 - 1. 컴퓨터와 베스킨라빈스 31 게임.


def baskin() :
    import random
    number = 0
    print('컴퓨터와 베스킨라빈스 31게임을 시작합니다.')
    while(True) :
        # 사용자
        my = input("사용자 차례입니다. 숫자를 입력하세요: ")
        my =  my.split() # 입력받은 숫자 공백 기준으로 자름
        # 아래줄 if의 첫번째 조건을 int(my[0]) != 1 이렇게 해놓아서
        # 계속 이어지지가 않았다 >> 첫번째가 1이 아니면 "숫자를 제대로 입력하세요"
        # 로 이어지게 됐던 것이다... 굳이 예제와같이 number로 해주어야하나? 했는데
        #  number로 해주어야 6라인의 number도 활성화된다.
        if int(my[0]) != number + 1 or len(my) > 3: # 입력 엉터리일시
            print("숫자를 제대로 입력하세요")
            continue
        if len(my) == 2 : # 숫자 2개입력되었을시
            if int(my[0]) + 1 != int(my[1]) :
                print("연속한 숫자만 입력가능")
                continue
        if len(my) == 3 : # 숫자 3개입력되었을시
            if int(my[0]) +1 != int(my[1]) or int(my[1]) + 1 != int(my[2]) :
                print("연속한 숫자만 입력가능")
                continue

        number = int(my[-1]) # 마지막 : -1
        print(f'현재 숫자 : {number}') # 변수대응으로 출력시 (f'내용.....{변수}....')

        if(number >= 31) : #사용자가 31일 외칠경우
            print('사용자 패배')
            break


        # 컴퓨터
        computer = list() # 빈 리스트 생성
        computer_turn_num = random.randint(1,3) # 컴퓨터가 1~3번 중 몇번 할지 랜덤하게 고름
        for i in range(computer_turn_num) :
            number += 1
            if number > 31 : # 컴퓨터가 31보다 큰수 외치면 1씩빼며 31로 만든다.
                number = number - 1
                continue
            computer.append(number) # 컴퓨터 리스트에 number 값 더해주기
            print(f'컴퓨터: {computer[-1]}')
        print(f'현재 숫자 : {number}')
        print() # 이건그냥.. 빈줄 한줄이군
        # 31 있는지 검사
        if 31 in computer :
            print("사용자 승리!")
            break
    print("게임 종료")
baskin()