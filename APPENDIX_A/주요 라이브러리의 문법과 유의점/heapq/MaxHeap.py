"""
파이썬에서는 최대 힙(Max Heap)을 제공하지 않는다.
따라서 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 입시로 변경하는 방식을 사용한다.
힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가,
힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.
"""

import heapq

def heapqsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapqsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)