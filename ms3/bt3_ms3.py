# 3 - 3. 숫자 2개 사이 짝수, 중앙값 출력
# 중앙값 : 정 중앙 값
# 자료 개수 홀수 : 가운데값 = 중앙값
# 자료 개수 짝수 : 가운데 두값 평균 = 중앙값
def find_even_number(n, m) :
    numbers = [i for i in range(n, m + 1)]  # range(시작 숫자, 끝 숫자 + 1)
    count = 0
    length = int(len(numbers))

    if length % 2 == 0 : # 자료 개수 짝수
        print('리스트의 자료 개수 짝수')
        print('리스트 길이는', length)
        for number in numbers:
            if number % 2 == 0: # 값이 짝수면
                print(int(count / 2 + 1), '번째 짝수 :', number)
                if count == length: # 그런데 그값이 중앙값이면
                    num1 = count + 1
                    num2 = count - 1
                    midnum = ((numbers.index(num1) + numbers.index(num2))/2)
                    print('중앙값은', int(midnum))
            count = count + 1
    else : # 자료 개수 홀수
        print('리스트의 자료 개수 홀수')
        print('리스트 길이는', length)
        for number in numbers:
            if number % 2 == 0: # 짝수면
                print(int(count/2+1), '번째 짝수 :', number)
                if count + 0.5  == length/2 :
                      midnum = int(numbers[count])
                      print('-> 중앙값이다! ', midnum)
            count = count + 1

# 입력
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)