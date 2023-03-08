"""
문제를 풀다보면, 입력을 최대한 빠르게 받아야 하는 경우가 있다.
흔히 정렬, 이진 탐색, 최단경로 문제의 경우 매우 많은 수의 데이터가 연속저으로 입력이 되곤 한다.
예를 들어 1,000만개가 넘는 라인이 입력되는 경우, 입력을 받는 것만으로도 시간 초과를 받을 수 있다.

입력의 개수가 많은 경우에는 단순히 input() 함수를 그대로 사용하지는 않는다.
파이썬의 기본 input() 함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문이다.
파이썬의 sys 라이브러리에 정의되어 있는 sys.stdin.readline()함수를 이용한다.

import sys
sys.stdin.readline().rstrip()
"""

# readline() 사용 소스코드 예시
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)