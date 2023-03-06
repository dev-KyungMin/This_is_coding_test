# 집합 자료형의 연산

# 집합 자료형의 연산으로는 합집합, 교집합, 차집합 연산이 있다.

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합