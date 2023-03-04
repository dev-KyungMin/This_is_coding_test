# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일때 0을 생략
a = -.7
print(a)

""" 지수를 이용한 파이썬의 지수 표현 방식 """

# 10억의 지수 표현 방식
a = 1e9
print(a)

#752.5
a = 75.25e1
print(a)

#3.954
a = 3954e-3
print(a)

""" 부등 소수점방식 """

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

""" round() 함수 이용 """

a = 0.3 + 0.6
print(round(a,4))

if(round(a,4) == 0.9):
    print(True)
else:
    print(False)