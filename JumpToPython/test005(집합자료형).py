#집합 자료형은 set 키워드를 사용해 만들 수 있다.

s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2)
# print(s2[0])  set은 인덱싱을 통해 자료형의 값을 얻을 수 없다. 즉 set은 순서가 없다

l1 = list(s2)  # list로 변환
print(l1[0])

t1 = tuple(s1) # tuple로 변환
print(t1[0])

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2) # 교집합 출력
print(s1.intersection(s2)) # intersection함수를 사용해도 가능
print(s1 | s2) # 합집합 출력
print(s1.union(s2)) # union 함수를 사용해도 가능
print(s1 - s2) # 차집합 출력
print(s1.difference(s2)) #difference 함수를 사용해도 가능

#집합 자료형 관련 함수
print(s1)
s1.add(7)   # 값 한개 추가
print(s1)
#s1.update(8) update는 1개 안됌 여러개해야함
s1.update([8, 9, 10])
print(s1)
