# 4 - 4. 주민번호 입력시
# 몇 년 몇 월 생인지 성별까지 출력 함수
# 주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
# 뒷자리는 1,3 은 남자 2,4는 여자
# 00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
# 뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

# 출력 예시
#
# a = "500629-2222222"
# check_id(a)
# 50년06월 여자
#
# a = "000629-2222222"
# check_id(a)
# 2000년 이후 출생자 입니까? 맞으면 o 아니면 x : o
# 잘못된 번호입니다.
# 올바른 번호를 넣어주세요
#
# a = "000629-2222222"
# check_id(a)
# 2000년 이후 출생자 입니까? 맞으면 o 아니면 x : x
# 00년06월 여자


def check_id(id_number):
    while True:
        if len(id_number) != 14 or id_number.find("-") == -1:
            print("잘못된 번호입니다.")
            break

        # 21 이하의 숫자로 시작하면 2000년 이후 출생인지 물어보기
        if int(id_number[:2]) <= 21:
            q = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
            # 2000년 이후 출생일 때
            if q == "o":
                if id_number[7] not in ["3", "4"]:
                    print("잘못된 번호입니다.")
                else:
                    if id_number[7] == "3":
                        gender = "남자"
                    else:
                        gender = "여자"
            # 아닐때 1900년 ~ 1921년 사이 출생일 때
            elif q == "x":
                if id_number[7] == "1":
                    gender = "남자"
                else:
                    gender = "여자"
            else:
                continue
        # 1922년 ~ 1999년 사이 출생일 때
        else:
            if id_number[7] not in ["1", "2"]:
                print("잘못된 번호입니다.")
            else:
                if id_number[7] == "1":
                    gender = "남자"
                else:
                    gender = "여자"
        year = id_number[:2]
        mon = id_number[2:4]
        try:
            print(f"{year}년{mon}월 {gender}")
        except:
            print("올바른 번호를 넣어주세요")
        break