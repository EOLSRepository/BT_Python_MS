# 📌Q2. 다음과 같이 학생들의 시험 답지가 있습니다. 그리고 답안지도 있습니다.
#
# 함수를 하나 만들어 채점을 하고 학생들의 점수를 출력하고 등수도 함께 출력해주세요.
#
# # 학생 답
# s = ["김갑,3242524215",
# "이을,3242524223",
# "박병,2242554131",
# "최정,4245242315",
# "정무,3242524315"]
#
# # 정답지
# a = [3,2,4,2,5,2,4,3,1,2]
#
#
# 🧐hint
# # 문자열도 숫자 정렬 가능
# a = ["5","2","3"]
# a.sort()
# ["2", "3", "5"]
# # 내림차순 정렬 가능
# a.sort(reverse=True)
# ["5", "3", "2"]
# ✅출력 예시
# grader(s, a)
# 학생: 정무 점수: 90점 1등
# 학생: 김갑 점수: 80점 2등
# 학생: 이을 점수: 70점 3등
# 학생: 박병 점수: 50점 4등
# 학생: 최정 점수: 40점 5등

def grader(student, answers):
    name = []  # 이름을 분리하여 저장할 리스트
    answer = []  # 학생들의 답을 분리하여 저장할 리스트
    scores = []  # 채점후 점수를 저장할 리스트
    for s in student:
        s = s.split(",")  # ,를 기준으로 이름과 정답지로 분리
        name.append(s[0])
        answer.append(s[1])

    score = 0
    # 점수 계산
    # 한 명씩 점수 계산, 답지와 내답이 같으면 10점 추가, 10문제라서 문제당 10점
    for a in answer:
        for i in range(len(a)):
            if int(a[i]) == answers[i]:
                score = score + 10
        scores.append(score)
        score = 0

    # 이름과 점수를 결합
    for i in range(len(name)):
        name[i] = str(scores[i]) + name[i]
    # 점수 기준 내림차순 정렬
    name.sort(reverse=True)

    # 한 사람씩 출력
    for i in range(len(name)):
        print(f"학생: {name[i][2:]} 점수: {name[i][:2]}점 {i + 1}등")