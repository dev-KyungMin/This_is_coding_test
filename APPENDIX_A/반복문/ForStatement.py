"""
 in 뒤에 온는 데이터에 포함되어 있는 모든 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문한다.
 in 뒤에 오는 데이터로는 리스트, 튜플, 문자열 등이 사용될 수 있다.

for 변수 in 리스트:
    실행할 소스코드
"""

# 1부터 9까지의 정수의 합을 구하는 예제를 동일하게 for문으로 작성한 코드

result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10): 
    """
    for문에서 수를 차례대로 나열할 때는 range()를 주호 쓰는데 
    range(시작 값, 끝 값 + 1) 형태 
    range() 의 값으로 하나의 값만을넣으면, 자동으로 시작 값은 0이 된다.
    주로 리스트나 튜플 데이터의 모든 원소를 첫 번째 인덱스부터 방문해야 할 때 이 방법을 사용한다.
    """
    result += i

print(result)


# 학생의 번호를 1번부터 매긴다고 했을 때, 다음과 같이 학생마다 합격 여부를 출력할 수 있다.
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")


"""
반복문 안에서 continue를 만나면 프로그램의 흐름은 반복문의 처음으로 돌아간다.
"""
print()
# 위의 예제에서 2번 학생과 4번 학생은 블랙리스트에 올라가 있어서 점수가 높아도 합격하지 못한다고 가정

scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

"""
반복문은 얼마든지 중첩해서 사용할 수 있다.

2중 반복문이 사용되어야 하는 대표적인 예시는 구구단

코딩 테스트에서도 '플로이드 위셜 알고리즘', '다이나믹 프로그래밍'등의 알고리즘 문제에서 많이 사용된다.
"""

print()

# 구구단 2단 부터 9단까지의 모든 결과를 출력하는 소스코드

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()