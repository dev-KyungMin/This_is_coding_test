# 집합 자료형 관련 함수

"""
add()       : 하나의 집합 자료형을 추가할 때
update()    : 여러 개의 값을 한꺼번에 추가하고자 할 떄
remove()    : 특정한 값을 제거할 때 

add(), remove() 함수는 모두 시간 복잡도가 O(1)
"""

data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

