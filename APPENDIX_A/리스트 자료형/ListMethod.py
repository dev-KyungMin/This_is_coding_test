"""
append()    변수명.append()             리스트에 원소를 하나 삽입할 때 사용한다.
sort()      변수명.sort()               기본 정렬 기능으로 오름차순으로 정렬한다.
            변수명.sort(reverse=True)   내림차순으로 정렬한다.
reverse()   변수명.reverse()            리스트의 원소의 순서를 모두 뒤집어 놓는다
insert()    변수명.insert(삽입할 위치      특정한 인덱스 위치에 원소를 삽입할 때 사용한다.
            인덱스, 삽입할 값)
count()     변수명.count(특정 값)         리스트에 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.
remove()    변수명.remove(특정 값)        특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다.
"""

a = [1, 4, 3]
print("기본 리스트 : ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입 : ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬 : ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬 : ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기 : ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가 : ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제 : ", a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set] 
print(result)