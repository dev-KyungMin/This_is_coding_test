# 리스트 컴프리헨션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

# 1  부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

"""
파이썬에서 언더바(_)의 역할 
반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.

예를 들어 1부터 9까지의 자연수를 더할 때는 예시처럼 작성하지만

summary = 0
for i in range(1, 10):
    summary += i
print(summary)

단순히 "Hello World"를 5번 출력할 때는 아래 예시처럼 언더바(_)를 이용하여 무시할 수 있다

for _ in range(5):
    print("Hello World")
"""
for _ in range(5):
    print("Hello World")