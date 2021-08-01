def rsp(my) : # 2주차 - 1. 컴퓨터와 가위바위보
    import random # 컴 가위바위보
    computer = random.randint(0, 2)  # 0 ~ 2 숫자를 랜덤으로 뽑아내는 코드
    if my == '가위' or my == '0' :#유저값  0.1.2 일시 가위바위보로 변경
        my = '가위'
        if computer == 2 :
            computer = '보'
            win = '사용자 승리!'
        elif computer == 1 :
            computer ='바위'
            win = '컴퓨터 승리!'
        else :
            computer = '가위'
            win = '무승부.'
        print('나:', my, '\n컴퓨터:', computer, '\n결과:', win)
    elif my == '바위' or my == '1' :
        my = '바위'
        if computer == 0 :
            computer = '가위'
            win = '사용자 승리!'
        elif computer == 2 :
            computer = '보'
            win = '컴퓨터 승리!'
        else :
            computer ='바위'
            win = '무승부.'
        print('나:', my, '\n컴퓨터:', computer, '\n결과:', win)
    elif my == '보' or my == '2' :
        my = '보'
        if computer == 1 :
            computer = '바위'
            win = '사용자 승리!'
        elif computer == 0 :
            computer = '가위'
            win = '컴퓨터 승리!'
        else :
            computer = '보'
            win = '무승부.'
        print('나:', my, '\n컴퓨터:', computer, '\n결과:', win)
    else :
        print('가위,바위,보,0,1,2 만 입력가능')
my = input('가위(또는 0)/바위(또는 1)/보(또는 2) 입력하시오 : ')
rsp(my)