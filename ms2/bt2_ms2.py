# 2 - 2. 월급 입력시 연봉 계산
def yearly_payment(monthly_payment) :
    monthly_payment = int(monthly_payment)
    before_payment = monthly_payment * 12
    if before_payment <= 1200 :
        tax = '6'
        after_payment = before_payment * 0.94
    elif before_payment <= 4600 :
        tax = '15'
        after_payment = before_payment * 0.85
    elif before_payment <= 8800 :
        tax = '24'
        after_payment = before_payment * 0.76
    elif before_payment <= 15000 :
        tax = '35'
        after_payment = before_payment * 0.65
    elif before_payment <= 30000 :
        tax = '38'
        after_payment = before_payment * 0.62
    elif before_payment <= 50000 :
        tax = '40'
        after_payment = before_payment * 0.60
    else :
        tax = '42'
        after_payment = before_payment * 0.58
    after_payment = int(after_payment)
    print('#출력\n', '세전 연봉:', before_payment, '만원\n','세율:', tax, '%\n', '세후 연봉:', after_payment, '만원')
monthly_payment = input('월급(만원단위) :')
yearly_payment(monthly_payment)
