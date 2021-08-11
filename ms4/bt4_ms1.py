# 4 - 1 . 숫자 입력받고 3자리마다 ',' 찍어주는 함수

def make_comma() :
    while True :
        number = input('숫자: ')
        try :
            int(number)
            break
        except :
            print('숫자 타입만 입력가능')
            continue
    newnum = 0
    if len(number) > 3: # 숫자 4자리로 들어올 경우부터 ',' 찍어줌
        count = len(number) / 3 # 몇 번 찍어야하는가
        index  = -1

        if len(number) % 3 == 0 :
            count = count - 1
            for num in number :
                print('여기까진들어옴1')
                while int(num) == number[count*3] :
                    print('여기까진들어옴2')

                    newnum = number[:len(number)-(3*count)] + ',' + number[len(number)-(3*count):]
                    index = index - 1

    print(newnum)
make_comma()