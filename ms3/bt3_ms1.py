# 1. 숫자 입력받아 구구단 출력
# 조건 : 홀 수 번째만 출력될 것
# 조건 :  값 50 이하까지 출력

def gugudan(num) :
    print('-- [', num, '] 단 50이하값 홀수번째 출력 시작--')
    count = 1
    while count < 10 :
        if num * count  <= 50 :
            print(num, 'X', count, '=', num * count)
            count = count + 2
    print ('---- 종료 ----')

num = int(input('구구단 출력할 숫자는 무엇?: '))
gugudan(num)
