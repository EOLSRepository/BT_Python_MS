# 4 - 2 . 특정 글자가 전체 글에 몇 개 있는지
# 개인 study용 정답 코드 보존, 기록입니다.
# 출력 예시
# a ="""안녕하세요.
# 반갑습니다. 파이썬 공부는 정말 재밌습니다.
# ""
#
# count_word(a, "습니다")
# 2


def count_word(text, word):
    # 문자열을 텍스트 파일로 저장
    text_save = open("text.txt", "w", encoding="UTF8")
    text_save.write(text)
    text_save.close()

    count = 0  # word를 세는 변수
    word_length = len(word)  # 문자의 길이
    word_save = ""  # 문자의 길이만큼만 저장

    f_1 = open("text.txt")  # 텍스트 파일 읽어오기
    for line in f_1:  # 한 줄씩 불러오기
        if word in line:  # 우리가 찾는 문자가 현재 문장에 있다면
            for s in line:
                word_save = word_save + s  # 한 글자씩 word_save에 저장
                if word_save == word:  # word_save와 word를 비교해서 같으면
                    count += 1  # count +1
                if len(word_save) == len(word):  # 다음 문자 저장을 위해 1칸씩 앞으로 이동
                    word_save = word_save[1:]
    print(count)  # word수 출력