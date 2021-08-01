# 2 - 3. 학생 이름, 점수 입력 >> 학점 출력 프로그램
def grader(name, score) :
    score=int(score)
    if score >= 95 and score <= 100 :
        grade = 'A+'
    elif score >= 90 and score <= 94 :
        grade = 'A'
    elif score >= 85 and score <= 89 :
        grade = 'B+'
    elif score >= 80 and score <= 84 :
        grade = 'B'
    elif score >= 75 and score <= 79 :
        grade = 'C+'
    elif score >= 70 and score <= 74 :
        grade = 'C'
    elif score >= 65 and score <= 69 :
        grade = 'D+'
    elif score >= 60 and score <= 64 :
        grade = 'D'
    else :
        grade = 'F'
    print('--결과--\n', '학생이름:', name, '\n점수:', score, '\n학점:', grade)
name = input('학생이름:')
score = input('점수:')
# score 값을 int 형변환하여 grader함수에 넣었더니 문법에러가 뜬다...
# >> 함수안에서 형변환 하는것으로 해결
# 같은 자료형 말고 각기 다른 자료형 여러개 매개변수에 넣으려면 어떻게 하나? 좀 더 알아보기
grader(name, score)