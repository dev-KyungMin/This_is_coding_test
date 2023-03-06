# 연산자

# 비교연산자

"""
X == Y  : X와 Y가 서로 같을 때 참(True)이다.
X != Y  : X와 Y가 서로 다를 때 참(True)이다.
X > Y   : X가 Y보다 클 때 참(True)이다.
X < Y   : X가 Y보다 작을 때 참(True)이다.
X >= Y  : X가 Y보다 크거나 같을 때 참(True)이다.
X <= Y  : X가 Y보다 작거나 같을 때 참(Treu)이다.
"""

# 논리연산자

"""
X and Y : X와 Y가 모두 참(True)일 때 참(True)이다.
X or Y  : X와 Y 중에 하나만 참(True)이어도 참(True)이다.
not X   : X가 거짓(False)일 때 참(True)이다.
"""

# 파이썬의 기타 연산자

"""
X in 리스트     : 리스트 안 에 X가 들어가 있을 때 참(True)이다.
X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 참(True)이다.
"""

# 디버깅하는 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분을 비워놓고 싶을 때 pass 문을 이용할 수 있다.

score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다.

score = 85
if score >= 80: result = "Success"
else: result = "Fail"
print(result)

# 조건부 표현식을 이용하면 if ~ else문을 한 줄에 작성해 사용할 수 있다.

score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# 특히 조건부 표현식은 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용할 수 있다.
# 일반적인 조건문의 경우
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3,5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)  

print(result)

# 위 코드를 아래와 같이 간단하게 작성할 수 있다
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)