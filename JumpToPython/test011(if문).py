# if 문 조건문
# 비교 연산자
# x < y	x가 y보다 작다
# x > y	x가 y보다 크다
# x == y	x와 y가 같다
# x != y	x와 y가 같지 않다
# x >= y	x가 y보다 크거나 같다
# x <= y	x가 y보다 작거나 같다
# x or y	x와 y 둘중에 하나만 참이어도 참이다
# x and y	x와 y 모두 참이어야 참이다
# not x	x가 거짓이면 참이다
# in	not in
# x in 리스트	x not in 리스트
# x in 튜플	x not in 튜플
# x in 문자열	x not in 문자열

pocket = ['card', 'money']
if 'card' in pocket:
    #print('버스타')
    pass
else:
    print('걸어가')

# 파이썬은 한줄로도 표현 가능하다
score = 90
message = "success" if score >= 60 else "failure"
print(message)