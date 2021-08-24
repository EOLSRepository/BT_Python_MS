# 📌Q4. 여러분은 어떤 상품을 판매하고 있습니다. 매월 상품을 많이 구매해준 VIP회원에게 할인 쿠폰을 제공해주려고 합니다. 아래와 같은 회원 정보가 있을 때 회원 정보를 출력하고 할인 쿠폰을 받을 회원이 누구인지 출력하는 함수를 만들어 주세요.
#
# 😲조건1 - 8회 이상 구매한 회원이 VIP대상
# 😲조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
# 😲조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것
#
# # 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
# info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
# ✅출력 예시
# good_customer(info)
# {'아이디': ['abc', 'cdb', 'bbc', 'ccb', 'dab', 'aab'], '나이': ['21세', '25세', '30세', '29세', '26세', '23세'], '전화번호': ['010-1234-5678', '000-0000-0000', '010-2222-3333', '000-0000-0000', '000-0000-0000', '010-3333-1111'], '성별': ['남자', '남자', '여자', '여자', '남자', '여자'], '지역': ['서울', '서울', '서울', '경기', '인천', '경기'], '구매횟수': [5, 4, 3, 9, 8, 10]}
# 할인 쿠폰을 받을 회원정보 아이디:aab, 나이:23세, 전화번호:010-3333-1111, 성별:여자, 지역:경기, 구매횟수: 10


def good_customer(info):
    # ,를 기준으로 분리
    info = info.split(",")
    # 정보를 담을 dict 생성
    info_dict = dict()
    # 정보 6개가 반복되므로 6으로 나눈 나머지를 이용하여 항목 구분하여 저장
    for i in range(len(info)):
        if i % 6 == 0:
            if info_dict.get("아이디", "") == "":
                info_dict["아이디"] = [info[i]]
            else:
                info_dict["아이디"].append(info[i])

        elif i % 6 == 1:
            if info_dict.get("나이", "") == "":
                info_dict["나이"] = [info[i]]
            else:
                info_dict["나이"].append(info[i])

        elif i % 6 == 2:
            if info_dict.get("전화번호", "") == "":
                info_dict["전화번호"] = [info[i]]
            else:
                info_dict["전화번호"].append(info[i])

        elif i % 6 == 3:
            if info_dict.get("성별", "") == "":
                info_dict["성별"] = [info[i]]
            else:
                info_dict["성별"].append(info[i])
        elif i % 6 == 4:
            if info_dict.get("지역", "") == "":
                info_dict["지역"] = [info[i]]
            else:
                info_dict["지역"].append(info[i])
        elif i % 6 == 5:
            if info_dict.get("구매횟수", "") == "":
                info_dict["구매횟수"] = [int(info[i])]
            else:
                info_dict["구매횟수"].append(int(info[i]))

    index = []  # 전화번호가 없는 회원의 인덱스 저장
    buy = []  # 구매횟수가 8회 이상인 회원 인덱스 저장
    for i in range(len(info_dict["전화번호"])):
        if info_dict["전화번호"][i] == "x":
            index.append(i)
            info_dict["전화번호"][i] = "000-0000-0000"
        if info_dict["구매횟수"][i] >= 8:
            buy.append(i)
    # 구매횟수가 8회 넘는 회원 중에 전화번호가 있는 회원 인덱스 저장
    true_index = []
    for i in buy:
        if i not in index:
            true_index.append(i)
    info_list = list(info_dict.items())

    # 정보 출력
    print(info_dict)
    for i in true_index:
        print(
            f"할인 쿠폰을 받을 회원정보 아이디:{info_list[0][1][i]}, 나이:{info_list[1][1][i]}, 전화번호:{info_list[2][1][i]}, 성별:{info_list[3][1][i]}, 지역:{info_list[4][1][i]}, 구매횟수: {info_list[5][1][i]}")