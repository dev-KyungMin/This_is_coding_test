"""
count_by_range(a, left_value, right_value) 함수
이는 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수르 반환한다.
다시 말해 원소의 값을 x라고 할 때, left_value <= x <= right_value인 원소의 개수를 O(logN)으로 빠르게 계산할 수 있다
"""

from bisect import bisect_left, bisect_right

# 값이 [legt_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 6))