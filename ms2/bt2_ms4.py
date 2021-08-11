def bus_fare(age, payment) : # 2 - 4. 나이,현금or카드 구분 >> 버스요금 계산 프로그램
    age = int(age)  # 나이 형변환 (string -> int)
# 나이에 따라 요금 나눔 (if...elif..else)
    if age < 8 or age >= 75 :
        money = '무료'
    elif age >= 8 and age < 14 :
        money = '450원'
    elif age >= 14 and age < 20 :
        if payment == '현금' :
            money = '1000원'
        else :
            money = '720원'
    elif age >= 20 and age < 75 :
        if payment == '현금' :
            money = '1300원'
        else :
            money = '1200원'
    print('=== 버스요금 결과 ===','\n나이:', age, '\n지불유형:', payment, '\n버스요금:', money)  # 출력
print('--- 버스요금 계산 ---') # 입력값 받고 유효성 검사
while True :  # 반드시 True 여야한다..true 는 안됨
    age = input('나이 :')
    try :
        int(age)
        break
    except :
        age = '오류'
    if age == '오류' :
        print('나이를 정수로 입력해야 합니다.')
while True :
    payment = input('지불수단은?(현금/카드):')
    if payment == '현금' or payment == '카드' :
        break
    else :
        print('현금 아니면 카드만 입력가능')
bus_fare(age, payment) # 버스값 계산 함수 bus_fare 에 사용자 입력값 전달