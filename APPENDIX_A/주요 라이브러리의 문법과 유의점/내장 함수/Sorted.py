"""
sorted() 함수는 iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다.
key 속성으로 정렬 기준을 명시할 수 있으며, 
reverse 속성으로 정렬된 결과 리스트를 뒤집을 지의 여부를 설정할 수 있다.
"""

result = sorted([9, 1, 8, 5, 4])                    # 오름차순으로 정렬
print(result)
result = sorted([9, 1, 8, 5, 4], reverse = True)    # 내림차순으로 정렬
print(result)