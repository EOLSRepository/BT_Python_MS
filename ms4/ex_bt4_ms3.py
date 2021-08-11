# 4 - 3. 코로나 식당 방명록에 잘못쓴 사람과 잘못된 번호를 출력하기
# 아래와 같은 방명록에서 잘못쓴것 이름, 번호 출력함수
# """"
# 방명록입니다.
#
# 김갑,123456789
# 이을,010-1234-5678
# 박병,010-5678-111
# 최정,111-1111-1111
# 정무,010-3333-3333
# """"

def wrong_guest_book(guest_book):
    # text 파일 저장
    text_save = open("guest_book.txt", "w", encoding="UTF8")
    text_save.write(guest_book)
    text_save.close()

    # 파일 불러오기
    file = open("guest_book.txt")
    for line in file:
        # 이름과 전화번호 구분
        name = line[:2]
        phone_number = line[3:].strip()
        # 조건을 만족하면 continue 아니면 출력
        if len(phone_number) == 13 and phone_number.find("-") != -1 and phone_number.startswith("010") == True:
            continue
        else:
            print(f"잘못 쓴 사람: {name}")
            print(f"잘못 쓴 번호: {phone_number}")
            print()


