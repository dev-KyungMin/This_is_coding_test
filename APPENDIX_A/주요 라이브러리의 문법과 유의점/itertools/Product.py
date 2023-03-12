"""
product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 테이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.
다만 원소를 중복하여 뽑는다.
product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.
product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
"""

from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 수열 구하기(중복 허용)

print(result)