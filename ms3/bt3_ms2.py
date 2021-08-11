# 3 - 2. 가위바위보
# 조건 : 게임 몇 판 진행할꺼? 입력 받는 기능
# 조건 : 0, 1, 2, "가위", "바위", "보" 이외 다른입력시 재입력 요구
# 조건 : 게임종료후 컴 vs 나 총 전적 출력

# 지난주 미션 가위바위도 코드를 수정하여 미션 진행하였습니다.
# 가위바위보 함수 시작
def rsp_advanced(my, count) :
    game_count = 1
    computer_win = 0
    computer_lose = 0
    user_win = 0
    user_lose = 0
    muu = 0
    while count - game_count >= 0 :
        import random # 컴 가위바위보
        computer = random.randint(0, 2)  # 0 ~ 2 숫자를 랜덤으로 뽑아내는 코드
        if my == '가위' or my == '0' :#유저값  0.1.2 일시 가위바위보로 변경
            my = '가위'
            if computer == 2 :
                computer = '보'
                win = '사용자 승리!'
                user_win = user_win + 1
                computer_lose = computer_lose + 1
            elif computer == 1 :
                computer ='바위'
                win = '컴퓨터 승리!'
                computer_win = computer_win +1
                user_lose = user_lose + 1
            else :
                computer = '가위'
                win = '무승부.'
                muu = muu + 1
        elif my == '바위' or my == '1' :
            my = '바위'
            if computer == 0 :
                computer = '가위'
                win = '사용자 승리!'
                user_win = user_win + 1
                computer_lose = computer_lose + 1
            elif computer == 2 :
                computer = '보'
                win = '컴퓨터 승리!'
                computer_win = computer_win + 1
                user_lose = user_lose + 1
            else :
                computer ='바위'
                win = '무승부.'
                muu = muu + 1
        elif my == '보' or my == '2' :
            my = '보'
            if computer == 1 :
                computer = '바위'
                win = '사용자 승리!'
                user_win = user_win + 1
                computer_lose = computer_lose + 1
            elif computer == 0 :
                computer = '가위'
                win = '컴퓨터 승리!'
                computer_win = computer_win + 1
                user_lose = user_lose + 1
            else :
                computer = '보'
                win = '무승부.'
                muu = muu + 1

        print('---', game_count, '번째 가위!바위!보! ---', '\n나:', my, '\n컴퓨터:', computer, '\n결과:', win)
        game_count = game_count + 1
    print('-- 종합적인 -->>', '컴퓨터', computer_win, '승', computer_lose, '패', muu, '무')
    print('-- 결과발표 -->>', '사용자', user_win, '승', user_lose, '패', muu, '무')
# 가위바위보 함수 정의 끝 #
# 가위바위보 횟수받기 #
while True :
    count = int(input('가위바위보를 몇 판 진행할까요 ? : '))
    if count < 0 :
        print('횟수는 1이상 정수만 입력가능')
        continue
    else :
        break
# 가위바위보 값받기 #
while True :
    my = input('가위(또는 0)/바위(또는 1)/보(또는 2) 입력하시오 : ')
    if my == '가위' or my == '바위' :
        break
    elif my == '보' :
        break
    elif my == '0' or my == '1' :
        break
    elif my == '2' :
        break
    else :
        print('가위,바위,보,0,1,2 만 입력가능')
        continue
# 가위바위보 함수 호출
rsp_advanced(my, count)