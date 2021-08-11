
#뿔테안경

# 3 - 4. 숫자 2개 입력하여 그사이 소수 갯수 출력
# 소수 : 1과 자기 자신만을 약수로 가지는 수
# 소수갯수 함수 시작
def count_prime_number() :
    # 입력
    while True:
        n = (input("첫 번째 수 입력 : "))
        try:
            int(n)
            break
        except:
            print('숫자로만 입력요망')
            continue
    while True:
        m = (input("두 번째 수 입력 : "))
        try:
            int(m)
            break
        except:
            print('숫자로만 입력요망')
            continue
    n = int(n)
    m = int(m)
    not_num = 0 # 소수가 아닌수 갯수.
    prime_num = 0 # 소수 갯수
    numbers = [i for i in range(n, m + 1)]  # range(시작 숫자, 끝 숫자 + 1)
    print(numbers, '중 소수의 갯수 구하기')
    if 1 in numbers : # 아래 for문 3부터 돌아가므로, 1과 2에 대한 처리
        print('1 : 소수가 아니다.')
        prime_num = prime_num - 1
        not_num = not_num + 1
    if 2 in numbers :
        prime_num = prime_num + 1
        print('2 : 소수!')
    for number in numbers :
        i = 2
        while i < number :
            if number % i == 0 :
                print(number, ': 소수가 아니다.')
                not_num = not_num + 1
                break
            elif number % i != 0 :
                if number - 1 == i :
                    print(number, ': 소수!')
                i = i + 1
                continue
    prime_num = len(numbers) - not_num
    print('전체', len(numbers), '개 중', not_num, '개의 숫자가 소수가 아니다.', '->> 소수개수:', prime_num)
# 소수갯수 함수 종료
count_prime_number()
