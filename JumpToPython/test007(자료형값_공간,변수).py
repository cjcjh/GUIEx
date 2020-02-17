from copy import  copy

# 변수 : 파이썬에서 사용하는 변수는 객체를 가리키는 것이라고 말할 수 있다.

a = [1, 2, 3]
print(id(a))    # a변수가 가리키는 메모리의 주소
b = a   # 리스트 복사
print(id(b))
print(a is b)   # a와 b가 가리키는 객체가 동일한가? : True
a[1] = 4
print(a)
print(b)

#[:] 사용
a = [1, 2, 3]
b = a[:]    # 리스트 a의 처음요소부터 끝 요소까지 슬라이싱
a[1] = 4
print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

# copy 모듈 사용
a = [1, 2, 3]
b = copy(a)  # b = a[:] 와 같다
print(a)
print(b)
print(id(a))
print(id(b))


#변수 만드는 여러가지 방법
a, b = ('python', 'life')
print(a)    # python
print(b)    # life

[a, b] = ['python', 'life']
print(a)    # python
print(b)    # life

a = b = 'python'
print(a)    #python
print(b)    #python

a = 3
b = 5
a, b = b, a     # a와 b의 값을 바꿈
print(a)    # 5
print(b)    # 3
